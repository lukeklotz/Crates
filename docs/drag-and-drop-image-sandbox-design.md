# Drag-and-Drop Image Sandbox — Design Brief

Design a mostly empty digital drafting board: calm, precise, and utilitarian.

## Color palette

| Purpose | Color |
| --- | --- |
| Application frame | Deep cobalt blue `#244394` |
| Canvas surface | Warm off-white `#FFFDE0` |
| Primary action / selection | Coral `#F06452` |
| Grid lines | Pale blue or white at 15–20% opacity |
| Canvas text | Near-black `#171717` |
| Frame text | Warm off-white `#FFFDE0` |

## Fonts

- **Interface and headings:** Space Grotesk, Arial, or Helvetica Neue. Use uppercase and bold weight; use a slightly condensed face when available.
- **Labels, coordinates, and file names:** IBM Plex Mono or JetBrains Mono.
- Avoid rounded, playful, or decorative typefaces.

## Single-page layout

```text
┌─────────────────────────────────────────────────────┐
│ PROJECT / SANDBOX                       + ADD IMAGE  │
├─────────────────────────────────────────────────────┤
│                                                     │
│        Large off-white drag-and-drop canvas         │
│        with faint engineering-grid lines.           │
│                                                     │
│       [ image ]       [ image ]                     │
│                    [ image ]                        │
│                                                     │
├─────────────────────────────────────────────────────┤
│  06 ITEMS    ZOOM 100%    GRID ON    CLEAR CANVAS   │
└─────────────────────────────────────────────────────┘
```

Use a cobalt-blue application frame around a large blank canvas.

- **Top bar:** project name and image-upload action.
- **Canvas:** off-white surface, faint visible grid, ample empty space.
- **Bottom status bar:** image count, zoom level, grid toggle, and canvas-clear control.

## Draggable-image behavior

- Do not put images in rounded cards. Give every image a thin border and a small monospace label beneath it.
- On selection, show a coral outline and compact coral resize handles.
- On hover, show minimal duplicate, rotate, and delete controls.
- Use a subtle shadow only while an image is being dragged.
- Offer optional snap-to-grid behavior.

## Design principle

The workspace should feel like a network engineer’s visual tool rather than a mood board: strict grid, bold color blocks, minimal controls, and plenty of empty space.
