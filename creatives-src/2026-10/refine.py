"""Clean a soft BiRefNet mask: drop specks, tighten the edge, 1px choke, feather, then
decontaminate edge colour so no white/background fringe remains."""
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi
from pymatting import estimate_foreground_ml

def clean_alpha(a, keep_frac=0.004):
    a = a.astype(np.float32)/255.
    b = a > .5
    lab, n = ndi.label(b)
    if n:
        areas = ndi.sum(b, lab, range(1, n+1))
        keep = np.isin(lab, 1+np.where(areas >= max(areas.max()*keep_frac, 400))[0])
        keep = ndi.binary_dilation(keep, iterations=4)
        a = a*keep
    # fill tiny pinholes inside the subject
    solid = ndi.binary_fill_holes(a > .5)
    holes = solid & ~(a > .5)
    lab, n = ndi.label(holes)
    if n:
        areas = ndi.sum(holes, lab, range(1, n+1))
        small = np.isin(lab, 1+np.where(areas < 150)[0])
        a[small] = 1
    a = np.clip((a-.18)/.64, 0, 1)                      # crisper edge, no haze
    a = cv2.erode(a, np.ones((3,3), np.uint8))          # 1px choke removes the halo
    a = cv2.GaussianBlur(a, (0,0), .8)                  # anti-aliased, seamless edge
    a[a < .02] = 0
    return a

def decontaminate(img, a):
    im = np.asarray(img.convert('RGB')).astype(np.float64)/255.
    h, w = a.shape; s = min(1., 1400/max(h, w))
    if s < 1:
        ims = cv2.resize(im, (int(w*s), int(h*s)), interpolation=cv2.INTER_AREA)
        as_ = cv2.resize(a, (int(w*s), int(h*s)), interpolation=cv2.INTER_AREA)
    else: ims, as_ = im, a
    F = estimate_foreground_ml(ims, as_.astype(np.float64))
    if s < 1: F = cv2.resize(F, (w, h), interpolation=cv2.INTER_CUBIC)
    # keep the original pixels where the subject is solid; use the estimate only at the edge
    wgt = np.clip((a-.6)/.35, 0, 1)[..., None]
    return np.clip(im*wgt + F*(1-wgt), 0, 1)
