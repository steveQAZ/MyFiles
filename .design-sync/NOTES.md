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

- Previews sit in one fixed 4:5 frame on the sunken surface so every format lines up.
- "Why it works" is a sunken callout with an Apple Green lightbulb badge, anchored level with the bottom of the preview. No left-border accent bars.
- Section headers: 11px uppercase overline, count pill on the right, 28px ghost buttons with icons.
- Ghost buttons: Slate Blue in light, `#D0D9E8` in dark (Slate Blue text is unreadable on dark).
- No keyboard-shortcut hint bar. Shortcuts may still work.
- Spacing: 16px panel padding and section gaps, 12px inside columns, 8px between stacked buttons.

## Social creatives (images, carousels, reel covers)

- Photos come from Google Drive `My Drive/AI/EWS/EWS Stock Photos` (Z:\My Drive\AI\EWS\EWS Stock Photos). When no photo there matches the topic (EV charger, Dalmatian, firefighters, NOC, warehouse), use a free-license Pexels or Pixabay photo, saved first to the Drive folder `27 Stock - Licensed (Pexels & Pixabay)`. Each photo must match the post's subject; keep watermarks and timestamp overlays out of frame.
- **Cut-out "sticker" style (from Oct 2026 v3):** remove the photo background and float the subject over a layered brand background (navy gradient + pattern + RF arcs or waves), with a soft drop shadow, and a floor shadow or green glow for depth. No plain photo rectangles, ovals or circles.
- Text never sits on the subject: text and cut-out keep separate zones. An occluder (clipboard card, caution tape, badge) may overlap the subject's body, never its head.
- **Never crop or cover a face or head.** Heads stay inside the canvas with room above; no text, logo or card covers them. The renderer QA checks detected faces on every export.
- Where a cut-out ends in a straight cut (the source photo's edge), that edge sits flush on the canvas edge or hides behind an occluder. A straight base is allowed only for objects standing on a floor shadow.
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
v3 (cut-out) layouts, current:

| Post | Layout |
|---|---|
| Oct 1 | Tilted equipment cut-out top-right on grid, green glow + front arc; text band below with side note |
| Oct 2 | (v2) Grid text column left, full-height photo right, green vertical seam |
| Oct 3 | Two climbers cut out, anchored bottom-left; title top full width; copy and CTA right |
| Oct 5 | Metering rack cut-out right on scan lines with sine waves; stacked 3-line title left |
| Oct 6 | Rack cut-out left with floor shadow; leader lines to white callout tags right |
| Oct 8 | Full-width team cut-out along the bottom; process dots row above |
| Oct 9 | Tall rack cut-out bleeding left; timeline and copy right |
| Oct 12 | (v2) Photo inside an app window (NOC title bar) |
| Oct 13 | Five layered sine waves behind title; worker cut-out bottom-right |
| Oct 15 | Full-width title; ECG line; crew cut-out bottom-right |
| Oct 16 | Giant 80% numeral; phone cut-out tilted over rings |
| Oct 19 | Worker (back view) cut-out right; chip stack left |
| Oct 20 | Crane cut-out with altitude ruler right edge |
| Oct 22 | DAS radio cluster cut-out top with "full bars" badge occluder; stadium seat curves |
| Oct 23 | Two-person cut-out bottom-right on diagonal glass stripes with floor shadow |
| Oct 26 | 3D hospital heat-map model floating, tilted, under the title |
| Oct 27 | 9-1-1 digit boxes; monopole cut-out right over contour lines |
| Oct 28 | Crew cut-out hanging from the top edge; centered text below |
| Oct 29 | Rotary phone cut-out bottom-left; terminal console card right |
| Oct 31 | Lattice tower cut-out on floor shadow, purple night glow, rings from the top |
| Oct 7 carousel | Cover: worker cut-out right, solid "5" numeral left |
| Oct 14 carousel | Cover: three-person cut-out rising from the bottom, chips row under title |
| Oct 21 carousel | Cover: two workers cut out above a caution-tape band; step 1 conduit cut-out behind a tape occluder |
| Oct 30 carousel | Cover: checklist card left overlapping two workers' shoulders, heads clear |
| Reel covers | Oct 4 floating floor-plan heat map in perspective + tag · Oct 11 antenna cut-out between oscilloscope waves · Oct 18 monopine cut-out with crosshair · Oct 25 lattice tower flush to top + build timeline |

v1/v2 layouts (retired, also do not repeat): Oct 1 angled photo top · Oct 3 circular photo · Oct 5 staggered triptych · Oct 6 rounded card + signal chain · Oct 8 viewfinder brackets · Oct 9 offset frame · Oct 13 sine-wave panel · Oct 15 text top + photo bottom · Oct 16 capsule photo · Oct 19 slanted photo · Oct 20 ruler + text band · Oct 22 wide photo + badge · Oct 23 window mullions · Oct 26 arch photo + 60+ · Oct 27 photo column + digit boxes · Oct 28 hexagon photo · Oct 29 terminal + fade · Oct 31 full-bleed photo + rings · carousel photo half-panels and photo covers · reel full-bleed photo covers.
