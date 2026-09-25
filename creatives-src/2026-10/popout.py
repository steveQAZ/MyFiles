"""Pop-out: keep the photo's lower part as a panel, remove only the negative space above
the cut line so the subject breaks out of the frame. mode 'full' = whole background removed."""
import sys, json, numpy as np, cv2
from PIL import Image
from refine import clean_alpha, decontaminate
SPEC = json.load(open('popspec.json'))
def build(k):
    s = SPEC[k]; src = s.get('src', k)
    img = Image.open(f'../render/ph/{src}.jpg').convert('RGB')
    mk = np.array(Image.open(f'soft/{src}.png').convert('L'))
    if s.get('mask') == 'oldonly':
        mk = np.array(Image.open(f'{src}.png').split()[-1])
    elif s.get('mask') == 'old':   # the lite model held together better on some thin frames
        mk = np.maximum(mk, np.array(Image.open(f'{src}.png').split()[-1]))
    a = clean_alpha(mk)
    if s.get('erase'):
        for x0, y0, x1, y1 in s['erase']:
            H, W = a.shape; a[int(y0*H):int(y1*H), int(x0*W):int(x1*W)] = 0
    F = decontaminate(img, a)
    H, W = a.shape
    x0, y0, x1, y1 = s.get('crop', [0, 0, 1, 1])
    X0, Y0, X1, Y1 = int(x0*W), int(y0*H), int(x1*W), int(y1*H)
    if s.get('mode', 'pop') == 'pop':
        yc = int(s['cut']*H)
        # soft 2px transition at the panel's top edge so the join is seamless
        ramp = np.clip((np.arange(H)[:, None]-yc+1)/2., 0, 1)*np.ones((1, W))
        ramp[:, :X0] = 0; ramp[:, X1:] = 0
        A = np.maximum(a, ramp)
        rgb = np.asarray(img).astype(np.float64)/255.
        wgt = (ramp > a)[..., None]
        C = np.where(wgt, rgb, F)
    else:
        A, C = a, F
    out = np.dstack([(C*255).round(), (A*255).round()]).astype(np.uint8)[Y0:Y1, X0:X1]
    im = Image.fromarray(out, 'RGBA')
    bb = im.getbbox(); im = im.crop(bb)
    sc = min(1., 1500/max(im.size))
    if sc < 1: im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    im.save(f'../render/pop/{k}.png')
    # panel geometry in output coords (fractions), for the renderer
    cut = None
    if s.get('mode', 'pop') == 'pop':
        cut = (yc-Y0-bb[1])/(bb[3]-bb[1])
    FJ = json.load(open('faces.json'))[src]
    bx = [(X0+bb[0])/W, (Y0+bb[1])/H, (X0+bb[2])/W, (Y0+bb[3])/H]
    faces = []
    for fx, fy, fw, fh, sc in FJ['faces']:
        u0 = (fx/FJ['w']-bx[0])/(bx[2]-bx[0]); v0 = (fy/FJ['h']-bx[1])/(bx[3]-bx[1])
        uw = fw/FJ['w']/(bx[2]-bx[0]); vh = fh/FJ['h']/(bx[3]-bx[1])
        if 0 <= u0+uw/2 <= 1 and 0 <= v0+vh/2 <= 1: faces.append([u0, v0, uw, vh])
    al = np.array(im)[:, :, 3] > 128; edge = {}
    if s.get('mode', 'pop') == 'pop':   # the panel's own sides are fine: only check the part above the cut line
        cy = int((yc-Y0-bb[1])); top = al.copy(); top[max(cy, 0):] = False
        sides = {'l': top[:, 0], 'r': top[:, -1], 't': al[0]}
    else:
        sides = {'l': al[:, 0], 'r': al[:, -1], 't': al[0], 'b': al[-1]}
    for e, v in sides.items():
        if v.mean() > .03:
            i = np.where(v)[0]; edge[e] = [round(i.min()/len(v), 3), round((i.max()+1)/len(v), 3)]
    return dict(faces=faces, edge=edge, w=im.width, h=im.height, cut=cut, mode=s.get('mode', 'pop'),
                src=src, box=[(X0+bb[0])/W, (Y0+bb[1])/H, (X0+bb[2])/W, (Y0+bb[3])/H])
if __name__ == '__main__':
    import os; os.makedirs('../render/pop', exist_ok=True)
    meta = json.load(open('../render/pop/meta.json')) if os.path.exists('../render/pop/meta.json') else {}
    for k in sys.argv[1:]:
        meta[k] = build(k); print(k, meta[k], flush=True)
    json.dump(meta, open('../render/pop/meta.json', 'w'), indent=1)
