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

- Photos come **only** from Google Drive `My Drive/AI/EWS/EWS Stock Photos` (Z:\My Drive\AI\EWS\EWS Stock Photos). Each photo must match the post's subject; crop to the subject and keep watermarks and timestamp overlays out of frame.
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
- No EV charger photos exist in the stock folder yet (Oct 5 used electrical metering gear).

### Layout registry: used, do not repeat
| Post | Layout |
|---|---|
| Oct 1 | Photo top with angled bottom edge and green seam; RF arcs bottom-right |
| Oct 2 | Grid text column left, full-height photo right, green vertical seam, dead-zone signal bars |
| Oct 3 | Large circular photo off-canvas right with green rings; stacked 4-line headline |
| Oct 5 | Staggered photo triptych top; green rule; text band below |
| Oct 6 | Rounded photo card left; vertical signal-chain nodes right |
| Oct 8 | Photo top with viewfinder brackets; 5-step numbered process row |
| Oct 9 | Dashed 1871 → 2026 timeline under the title; offset-framed photo right |
| Oct 12 | Photo inside an app window (NOC title bar, live dot); sparkline divider |
| Oct 13 | Full-bleed photo; navy panel with sine-wave top edge |
| Oct 15 | Text top on grid; ECG pulse divider; photo bottom |
| Oct 16 | Giant stat numeral; photo in tall capsule with rings |
| Oct 19 | Photo right with slanted edge and green seam; role chips stack |
| Oct 20 | Altitude ruler scale left of photo; text band below |
| Oct 22 | Wide photo top with "full bars" badge; chips row |
| Oct 23 | Photo right with navy window-mullion bars over it |
| Oct 26 | Giant "60+" numeral; arch-shaped photo; tick list |
| Oct 27 | Full-height photo column left; 9-1-1 digit boxes; contour lines |
| Oct 28 | Centered hexagon photo with radiating arcs; centered text |
| Oct 29 | Terminal console block; photo bottom-right fade |
| Oct 31 | Full-bleed photo, dark fade, centered headline, rings from tower |
| Oct 7 carousel | Solid "5" numeral cover; floorplan slides highlighting one room each |
| Oct 14 carousel | Phrasebook slides: code term, "in plain English", line-art icon per code |
| Oct 21 carousel | Caution-tape stripe system; step labels; photo half-panels |
| Oct 30 carousel | Clipboard card cover; checkbox progress slides with "why it matters" panel |
| Reel covers | Oct 4 photo + 2×2 step grid · Oct 11 oscilloscope waves · Oct 18 crosshair target · Oct 25 single photo + 4-step build timeline |
