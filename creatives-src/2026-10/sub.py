"""Full-size subject layer: same pixel grid as the source photo, alpha = cleaned subject mask,
edge colours decontaminated. The renderer stacks it exactly on top of the photo."""
import sys, json, os, numpy as np
from PIL import Image
from refine import clean_alpha, decontaminate
SPEC = json.load(open('subspec.json'))
os.makedirs('../render/sub', exist_ok=True)
for k in sys.argv[1:] or SPEC:
    s = SPEC.get(k, {})
    img = Image.open(f'../render/ph/{k}.jpg').convert('RGB')
    mk = np.array(Image.open(f'soft/{k}.png').convert('L'))
    if s.get('mask') == 'old': mk = np.maximum(mk, np.array(Image.open(f'{k}.png').split()[-1]))
    if s.get('mask') == 'oldonly': mk = np.array(Image.open(f'{k}.png').split()[-1])
    a = clean_alpha(mk)
    H, W = a.shape
    for x0, y0, x1, y1 in s.get('erase', []):
        a[int(y0*H):int(y1*H), int(x0*W):int(x1*W)] = 0
    F = decontaminate(img, a)
    out = np.dstack([(F*255).round(), (a*255).round()]).astype(np.uint8)
    Image.fromarray(out, 'RGBA').save(f'../render/sub/{k}.png', optimize=True)
    print(k, flush=True)
