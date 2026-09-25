"""Full-size subject layer: same pixel grid as the source photo, alpha = cleaned subject mask,
edge colours decontaminated. The renderer stacks it exactly on top of the photo."""
import sys, json, os, numpy as np
from PIL import Image
from refine import clean_alpha, decontaminate
SPEC = json.load(open('subspec.json'))
FACES = json.load(open('faces.json'))
os.makedirs('../render/sub', exist_ok=True)
for k in sys.argv[1:] or SPEC:
    s = SPEC.get(k, {})
    img = Image.open(f'../render/ph/{k}.jpg').convert('RGB')
    mk = np.array(Image.open(f'soft/{k}.png').convert('L'))
    if s.get('mask') == 'old': mk = np.maximum(mk, np.array(Image.open(f'{k}.png').split()[-1]))
    if s.get('mask') == 'oldonly': mk = np.array(Image.open(f'{k}.png').split()[-1])
    a = clean_alpha(mk)
    # solid interior: anything clearly inside the subject is fully opaque; only the outer edge stays soft
    from scipy import ndimage as ndi
    solid = ndi.binary_erosion(a > .3, iterations=2)
    a = np.maximum(a, ndi.gaussian_filter(solid.astype(np.float32), .8))
    H, W = a.shape
    for x0, y0, x1, y1 in s.get('erase', []):
        a[int(y0*H):int(y1*H), int(x0*W):int(x1*W)] = 0
    # protect every detected head: inside a head ellipse, even a faint mask response counts as subject
    soft = mk.astype(np.float32)/255.
    yy, xx = np.mgrid[0:H, 0:W]
    for fx, fy, fw, fh, _ in FACES.get(k, {}).get('faces', []):
        cx, cy, rx, ry = fx+fw/2, fy+fh*.3, fw*.75, fh*1.05
        box = (slice(max(0, int(cy-ry)), min(H, int(cy+ry)+1)), slice(max(0, int(cx-rx)), min(W, int(cx+rx)+1)))
        e = ((xx[box]-cx)/rx)**2+((yy[box]-cy)/ry)**2 < 1
        boost = np.clip((soft[box]-.03)/.12, 0, 1)
        a[box] = np.where(e, np.maximum(a[box], boost), a[box])
    F = decontaminate(img, a)
    out = np.dstack([(F*255).round(), (a*255).round()]).astype(np.uint8)
    Image.fromarray(out, 'RGBA').save(f'../render/sub/{k}.png', optimize=True)
    print(k, flush=True)
