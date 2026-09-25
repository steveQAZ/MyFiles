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
- **Pop-out style (from Oct 2026 v4):** don't remove the whole background. Keep the lower part of the photo (floor, ground, table, desk) as a panel and remove only the negative space above the cut line, so the subject breaks out of the frame. Remove the entire background only for isolated objects (3D models, a crane, a radio cluster, conduit) and then always put a big EWS brand graphic behind them.
- A big brand graphic sits behind every subject for depth: concentric Slate/Green rings, a solid Apple Green disc, giant signal bars, broadcast arcs, a Slate hexagon, a thick sine band or a slanted green slab. Use a different one from the neighbouring posts.
- Cut edges must be seamless: soft mask from BiRefNet, specks removed, 1px choke, 0.8px feather and edge colour decontamination. No white fringe or stray particles.
- Text never sits on the subject: text and subject keep separate zones. An occluder (clipboard card, caution tape, badge, filing tag) may overlap the subject's body, never its head.
- **Never crop or cover a face or head.** Heads stay inside the canvas with room above; no text, logo or card covers them. The renderer QA checks detected faces on every export.
- Where a subject is cut by the photo's own edge above the panel, that edge sits flush on the canvas edge or hides behind an occluder. The panel's own straight edges are fine.
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
v4 (pop-out) layouts, current. Each has a big brand graphic behind the subject:

| Post | Layout |
|---|---|
| Oct 1 | Equipment popping out of a gravel panel, top-right; Slate/Green rings behind |
| Oct 2 | (v2) Grid text column left, full-height photo right |
| Oct 3 | Climbers break out of a bottom-left panel; green disc behind their heads |
| Oct 5 | Metering rack on a gravel panel, bottom-right; giant signal/charge bars behind |
| Oct 6 | Rack panel flush left with its top strip popping out; leader lines to tags; Slate hexagon |
| Oct 8 | Team on a floor strip across the bottom; broadcast arcs behind |
| Oct 9 | Rack room panel bottom-left, rack top popping out; slanted green slab |
| Oct 12 | (v2) Photo inside an app window (NOC title bar) |
| Oct 13 | Worker full cut-out flush bottom-right over a thick Slate/Green sine band |
| Oct 15 | Crew on a ground strip bottom-right; rings behind; ECG line |
| Oct 16 | Phone popping off a carpet panel; broadcast arcs; giant 80% |
| Oct 19 | Worker (back) on a ground strip, right; Slate hexagon |
| Oct 20 | Crane flush to the top; its base hidden behind an "FAA filing first" tag; rings |
| Oct 22 | DAS radio cluster floating top-left; giant signal bars and "full bars" badge |
| Oct 23 | Two men over their conference table panel, bottom-right; green slab |
| Oct 26 | 3D hospital model tilted over a Slate hexagon |
| Oct 27 | Monopole rising from its compound panel, right; broadcast arcs from the top |
| Oct 28 | Crew in tower steel flush to the top; green disc; centered text below |
| Oct 29 | Rotary phone on a desk panel, bottom-left; sine band; LOGIN terminal card |
| Oct 31 | Lattice tower flush bottom-right on floor shadow; broadcast arcs; night glow |
| Oct 7 carousel | Cover: worker on a ground panel, right; green disc; "5" numeral |
| Oct 14 carousel | Cover: team at their table (table kept), rings behind heads |
| Oct 21 carousel | Cover: crew at the pole base panel, green slab behind, tape band; step 1 conduit behind a tape occluder |
| Oct 30 carousel | Cover: two men on a rock panel, Slate hexagon; checklist card overlaps a shoulder only |
| Reel covers | Oct 4 floating floor-plan heat map · Oct 11 antenna over a sine band · Oct 18 monopine on its building panel, green disc, crosshair · Oct 25 lattice tower flush to top over its building panel, hexagon |

v3 cut-out layouts (retired, also do not repeat): whole-background cut-outs floating with drop shadows, same compositions as above without the photo panels.

v1/v2 layouts (retired, also do not repeat): Oct 1 angled photo top · Oct 3 circular photo · Oct 5 staggered triptych · Oct 6 rounded card + signal chain · Oct 8 viewfinder brackets · Oct 9 offset frame · Oct 13 sine-wave panel · Oct 15 text top + photo bottom · Oct 16 capsule photo · Oct 19 slanted photo · Oct 20 ruler + text band · Oct 22 wide photo + badge · Oct 23 window mullions · Oct 26 arch photo + 60+ · Oct 27 photo column + digit boxes · Oct 28 hexagon photo · Oct 29 terminal + fade · Oct 31 full-bleed photo + rings · carousel photo half-panels and photo covers · reel full-bleed photo covers.
