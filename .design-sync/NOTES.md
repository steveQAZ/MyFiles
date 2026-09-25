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
- **Break-out photos (from Oct 2026 v7).** Keep the photo, but dissolve its background away from the subject so the subject breaks out over the navy. Never remove the whole background: the ground, floor or table stays, inside soft organic blobs.
- **No visible crop lines, ever.** No rectangles, no straight gradient edges. Wherever a photo ends inside the canvas, it dissolves along a noisy, organic edge; the only straight edges allowed are the canvas edges themselves. A viewer should not be able to tell where the photo was cut.
- **Subject layer:** same pixels as the photo, background removed with a soft BiRefNet mask, specks removed, 1px choke and edge colour decontamination, solid interior, and every detected head protected so hair is never clipped.
- **Sandwich depth with bold graphics:** each post's graphic is drawn twice, behind the subject and (clipped to one side of a line) in front of it. Graphics are highly visible: 6–12px strokes, full Apple Green and white, green glow, plus a drop shadow on the front copy. They never cross text or a face.
- **Never reuse a graphic.** Similar ideas are fine; identical graphics are not. Check the graphics registry below.
- **Depth stack, back to front:** navy base with a pattern → photo background (graded) → back copy of the post's graphic → subject layer with drop shadow → front copy of the graphic → frosted glass cards → text.
- Text sits on the navy or on dissolved background, never on the subject.
- **Never crop or cover a face or head.** Heads stay inside the solid part of the photo panel or the subject layer, with room above; no text, logo, card or front graphic covers them. The renderer QA checks detected faces on every export.
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
v7 layouts, current. Same text and section positions as the v5 table below, now with organic photo dissolves and these one-off graphics:

| Post | Graphic (sandwiched) |
|---|---|
| Oct 1 | Flattened broadcast rings around the equipment |
| Oct 2 | Red dashed dead-zone circle with an X over the racking |
| Oct 3 | Climbing rope curve, behind the first climber, in front of the second |
| Oct 5 | Double lightning bolt through the rack |
| Oct 6 | Vertical signal chain with four nodes through the rack |
| Oct 8 | Wide green ribbon arc along the team's feet |
| Oct 9 | Clock-dial ellipse with 12 ticks around the rack |
| Oct 12 | Radar sweep with wedge over the NOC desk |
| Oct 13 | Wind streaks across the worker's shoulders |
| Oct 15 | ECG pulse bent into a ring around the crew |
| Oct 16 | Three Wi-Fi arcs over the phone |
| Oct 19 | Flattened hexagon around the worker's head |
| Oct 20 | Dashed flight path with arrowhead across the crane |
| Oct 22 | Equalizer bars rising behind the radio cluster |
| Oct 23 | Three glass panes between and in front of the two men |
| Oct 26 | Stacked perspective contour rings under the 3D model |
| Oct 27 | Three sonar rings stacked along the monopole |
| Oct 28 | Shield outline around the crew in the tower |
| Oct 29 | Ring of rotating data bits around the handset |
| Oct 31 | Double helix climbing the tower |
| Oct 7 carousel | Ring with five nodes around the worker (one node per area) |
| Oct 14 carousel | Giant code braces around the team |
| Oct 21 carousel | Dimension line with arrows across the trench; slides 2 and 4 bent conduit lines (3 and 2 lines) |
| Oct 30 carousel | Big check stroke inside a dashed inspection circle |
| Reel covers | Oct 4 perspective floor grid through the antenna canopy · Oct 11 green/orange oscilloscope waves through the antenna · Oct 18 crosshair with corner brackets on the monopine · Oct 25 rising dotted path with four nodes up the tower |

v6 and earlier layouts: retired, do not repeat.


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
