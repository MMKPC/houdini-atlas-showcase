# Proof Packet — SOP Data Foundations

> Fill this in after building the network. Paste the completed copy
> into Atlas under `/proof-packets` for the demo session
> `demo.sop_table_in_18`.

## Identity

- Learner key: `default`  *(or your own if you have set one)*
- Houdini version:
- Date:
- Estimated build time:

## Screenshots (4 required)

1. **Network view.** Shows: grid1 → wr_height → wr_color, with two
   branches into `OUT_data_view` and into the promote chain
   `promote_pt_to_prim_avg` → `promote_prim_to_pt_max` → `OUT_render_ready`.
   *File:* `01_network.png`

2. **Geometry Spreadsheet (Points tab).** Shows: 400 rows. Visible columns:
   `P`, `@height`, `@Cd`. `@height` values inside `[-1.0, 1.0]`.
   *File:* `02_spreadsheet_points.png`

3. **Geometry Spreadsheet (Primitives tab) on `promote_pt_to_prim_avg`.** Shows:
   361 rows. Visible columns: `@height` (now smoother than the point version).
   *File:* `03_spreadsheet_prims.png`

4. **Viewport on `OUT_render_ready`.** Shows: cool-warm gradient driven by
   the promoted `@height` — note the stair-step effect at island borders.
   *File:* `04_viewport_render_ready.png`

## Four answers (1 line each)

1. *Why are Points and Primitives row counts different here?*

2. *After Attribute Promote (point→prim, average), is `@height` on points,
   prims, or both? What does the spreadsheet say?*

3. *After Attribute Promote (prim→point, max), where does the visible
   stair-step come from?*

4. *Which class is `@ptnum` meaningful in, and which class is `@primnum`
   meaningful in? Cite the spreadsheet tab.*

## Failure log (be honest)

- What went wrong the first time?
- Which step did you skip and have to come back to?
- What did the spreadsheet teach you that the viewport hid?

## Self-rating (optional, learner-entered)

- Confidence I could rebuild this from scratch tomorrow: **___ / 5**
- Confidence I could explain promotion to another learner: **___ / 5**
- Notes for next session:
