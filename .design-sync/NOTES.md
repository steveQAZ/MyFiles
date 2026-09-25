# Design notes: EWS

Decisions from design reviews that later design work and syncs must follow. The source of truth for the brand is the **EWS Design System** artifact (https://claude.ai/artifact/EpdYZufByTNtnxjiWF3sdv); its README section "App & dashboard patterns" holds the full rules below.

No design-system sync has run from this repo yet: it holds no component library. EWS work so far is the October 2026 campaign review board (https://claude.ai/artifact/QuPAqdA9Ru47XKXXwgFyfZ).

## Always

- Build EWS pages from the EWS Design System: Montserrat (400/500/600/700/900), Slate Blue `#3C5072`, Apple Green `#84C73D`, Gunmetal `#434853`, Off-White `#FEFEFE`, 4px buttons and inputs, 8px cards, Slate-tinted shadows, Lucide icons.
- Status colors: Approved `#84C73D`, Revisions `#E88A20`, Declined `#D03030`.

## App header (review boards, dashboards)

- Keep the header on the page surface. Do **not** put an app header on a Slate Blue band or use the two-line white/green hero headline there. A Slate Blue band was tried on the October board and rejected.
- Layout: logo | title + meta line | progress meter, split by 1px hairlines. Midnight Blue logo in light, Ghost White in dark.
- Title on one line, uppercase, weight 900, last word in Apple Green ("OCTOBER CAMPAIGN").

## Tiles

- Tile headline line two is Apple Green: `#84C73D` in dark theme, `#3F6D18` in light theme (Apple Green on white is 2.1:1).
- Every tile shows a format icon: `image` for Image, stacked squares for Carousel, `play` for Reel.
- Status = colored border + icon badge, never color alone.

## Detail panel

- Previews hug the creative: 1:1 for images, 4:5 for carousels, 9:16 for reels. No frame, no letterbox bands.
- "Why it works" is a sunken callout with an Apple Green lightbulb badge, anchored level with the bottom of the preview. No left-border accent bars.
- Section headers: 11px uppercase overline, count pill on the right, 28px ghost buttons with icons.
- Ghost buttons: Slate Blue in light, `#D0D9E8` in dark (Slate Blue text is unreadable on dark).
- No keyboard-shortcut hint bar. Shortcuts may still work.
- Spacing: 16px panel padding and section gaps, 12px inside columns, 8px between stacked buttons.

## Social creatives (images, carousels, reel covers)

- Photos come from Google Drive `My Drive/AI/EWS/EWS Stock Photos` (Z:\My Drive\AI\EWS\EWS Stock Photos). When no photo there matches the topic (EV charger, Dalmatian, firefighters, NOC, warehouse), use a free-license Pexels or Pixabay photo, saved first to the Drive folder `27 Stock - Licensed (Pexels & Pixabay)`. Each photo must match the post's subject; keep watermarks and timestamp overlays out of frame.
- **Full photos, never background-removed (from Oct 2026 v5).** Each photo sits in its own section of the canvas (a side column, a top or bottom band, or a corner block), balanced against the text section.
- **Depth stack, back to front:** navy base with a pattern → graded photo section (navy multiply + soft-light tint) with a gradient fade into the navy on the side facing the text → brand overlay crossing the seam (RF arcs, waves, ECG, dashed timelines, with a green glow) → frosted glass cards (blur, thin light border, deep shadow) overlapping the photo edge → text.
- The photo's hard edge never shows on the text side: it always fades out through a gradient mask. Canvas edges may cut the photo.
- Text sits on the navy side or the faded part of the gradient, never on the solid photo. Glass cards and brand overlays may sit over the photo.
- **Never crop or cover a face or head.** Heads stay inside the solid (unfaded) part of the photo section with room above; no text, logo or card covers them. The renderer QA checks detected faces on every export.
- Style: EWS navy (`#2A3852` / `#1C1F26`), uppercase Montserrat 900 headline with the second line in Apple Green, green CTA block, white logo, phone + engineeringwireless.com. Text and photo are clearly separated, and the text side carries a technical background: blueprint grid, RF arcs, sine waves, contour lines, lattice, or dot matrix.
- **Permanent spec (every graphic):** 64px margin on all four sides; all text, logos and buttons stay inside it (photos may bleed to the edge).
- **Fixed type sizes, never changed per post:** kicker 22px · title 76px (Montserrat 900) · subtext 28px · CTA 26px · labels/chips 22px · footer 24px · big numerals 200px. Titles wrap onto more lines rather than shrink. Logo 150px wide at the top-left margin (carousel slide footers use 100px).
- **Website is always written `EngineeringWireless.com`** (capital E and W). Phone: `+1 (480) 968-6000`.
- **Never stretch a photo.** Only uniform scaling or cropping (object-fit: cover or a uniform zoom). Flag any photo enlarged more than 1.25x.
- **One photo is used once per post.** A carousel never repeats a photo across its slides, and one photo is never split into a fake before/after.
- **No outlined or stroked text.** Numerals and headlines are solid fills.
- **Crop out third-party logos and watermarks** (for example Top Workplaces, Centra, drink labels, #surgevisions).
- No decorative diagrams that don't carry information.
- Leave at least 8px between any two text elements; the renderer QA checks margins, spacing, overflow, font sizes, photo scaling and photo reuse on every export.
- **Never reuse a layout.** Every post gets a composition that hasn't been used before. Check the registry below and add new ones to it.
- Sizes: 1080×1080 images, 1080×1350 carousel slides, 1080×1920 reel covers.
- No EV charger, Dalmatian or firefighter photos exist in the stock folder yet. Oct 1, 5 and 28 use interim EWS cut-outs until Pexels/Pixabay photos are added.

### Layout registry: used, do not repeat
v5 layouts, current (full photo sections with gradient fades, seam overlays and glass cards):

| Post | Layout |
|---|---|
| Oct 1 | Photo block bottom-right fading up and left; RF rings over it; glass "public safety radio" card; text top-left |
| Oct 2 | Photo column left with a diagonal navy wash; glass dead-zone meter over the photo; text right |
| Oct 3 | Photo band top with a green ruler seam; glass question card over the photo; title below |
| Oct 5 | Photo block bottom-right fading up and left; ECG spark line across; glass "2026 theme" card |
| Oct 6 | Photo column right; glowing leader lines from glass tags on the left into the rack |
| Oct 8 | Team photo band bottom; glowing process dots above; arcs rising from the bottom |
| Oct 9 | Photo column left; dashed 1871→2026 line crossing the whole canvas; glass "since 1925" card |
| Oct 12 | Photo band top fading down; glowing sparkline seam; glass "live" status pill |
| Oct 13 | Photo column right; storm sine waves across the bottom; glass "before the storm" card |
| Oct 15 | Photo column right; ECG line across the bottom |
| Oct 16 | Photo corner top-right fading left and down; RF rings; giant 80% over the fade |
| Oct 19 | Photo band top with a left navy wash; glass chips row below |
| Oct 20 | Crane band top (zoomed to leave out the trucks); glass FAA filing card on the seam; arcs from the corner |
| Oct 22 | Full-bleed radio-cluster photo with a diagonal navy wash; big glass signal-bars card |
| Oct 23 | Photo column left; glass Low-E card on the seam; text right |
| Oct 26 | 3D heat-map band across the middle, fading top and bottom; glass "predicted" card |
| Oct 27 | Monopole column right; glass 9-1-1 digit tiles; contour lines |
| Oct 28 | Crew band top; arcs from the seam; centered text below |
| Oct 29 | Phone column right; glass terminal card overlapping the seam |
| Oct 31 | Sunset tower column right with a wide fade; RF rings from the tower top |
| Oct 7 carousel | Cover: worker photo top-right fading left and down; "5" numeral over the fade |
| Oct 14 carousel | Cover: team-at-table block bottom-right; glass code chips stacked over the seam |
| Oct 21 carousel | Cover: trench photo bottom-right with a diagonal caution tape across it; slides 2 and 4 photo columns right with a tape seam |
| Oct 30 carousel | Cover: crew photo band bottom; clipboard card above, overlapping the seam |
| Reel covers | Oct 4 photo block bottom, glass 2×2 steps above · Oct 11 photo top-left with glowing waves at the seam · Oct 18 photo right with crosshair · Oct 25 photo right, glowing vertical step timeline left |

v4 pop-out layouts and v3 cut-out layouts: retired, do not repeat.

v1/v2 layouts (retired, also do not repeat): Oct 1 angled photo top · Oct 3 circular photo · Oct 5 staggered triptych · Oct 6 rounded card + signal chain · Oct 8 viewfinder brackets · Oct 9 offset frame · Oct 13 sine-wave panel · Oct 15 text top + photo bottom · Oct 16 capsule photo · Oct 19 slanted photo · Oct 20 ruler + text band · Oct 22 wide photo + badge · Oct 23 window mullions · Oct 26 arch photo + 60+ · Oct 27 photo column + digit boxes · Oct 28 hexagon photo · Oct 29 terminal + fade · Oct 31 full-bleed photo + rings · carousel photo half-panels and photo covers · reel full-bleed photo covers.
