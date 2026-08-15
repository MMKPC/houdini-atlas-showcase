# Proof Packet — Curve Skeleton / Alien Limb

> Fill in after building the limb. Paste into Atlas /proof-packets for
> `demo.copy_segments_along_curve_07`.

## Identity

- Learner key: `default`
- Houdini version:
- Date:

## Screenshots (5 required)

1. **Network view.** Shows: csv_import → make_polyline → resample →
   wr_seg_id → wr_orient → wr_width_scale → copy_to_points → OUT_alien_limb.
   *File:* `01_network.png`

2. **Spreadsheet on `wr_orient`, Points tab.** Columns visible: `P`, `N`,
   `@seg_id`, `@orient` (4 components), `@curveu`. 64 rows.
   *File:* `02_spreadsheet_orient.png`

3. **Viewport at `up_axis = (0,1,0)`.** Capsules along the limb, no flips.
   *File:* `03_viewport_up_y.png`

4. **Viewport at `up_axis = (0,0,1)`.** Same limb, capsules rotated as
   expected, **no 180° flips** anywhere along the curve.
   *File:* `04_viewport_up_z.png`

5. **Spreadsheet on `wr_width_scale`** showing `@pscale` runs from ~1.0 at
   the base to ~0.22 at the tip.
   *File:* `05_spreadsheet_pscale.png`

## Three answers (1 line each)

1. *Why does the standard `up = (0,1,0)` trick fail when the curve passes
   through a tangent of `(0,1,0)`? Reference your snippet by line.*

2. *What attribute did you freeze in `wr_seg_id`, and what would happen
   downstream if you skipped it?*

3. *Where in the snippet does `@curveu` enter the width calculation, and
   why is it preferred over `@ptnum`?*

## Failure log

- Did the limb flip during the up-vector sweep? On which segments?
- Did segment ids reorder when you changed an upstream parameter?
- What did the spreadsheet teach you that the viewport hid?

## Self-rating (optional, learner-entered)

- Confidence I could rebuild this from scratch tomorrow: **___ / 5**
- Confidence I could fix this on someone else's broken limb: **___ / 5**
