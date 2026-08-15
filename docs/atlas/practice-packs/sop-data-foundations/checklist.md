# SOP Data Foundations — Build Checklist

Tick each box only after you can point at the proof on screen.

## Phase 1 — Network skeleton

- [ ] **1. Create a Geometry SOP.** Name it `geo_sop_foundations`. Dive inside.
- [ ] **2. Create a Grid.** Rows 20, Columns 20, Size 10×10. Name it `grid1`.
      Confirm in the spreadsheet: 400 points, 361 primitives.
- [ ] **3. Append an Attribute Wrangle.** Run over: **Points**.
      Paste `vex_height_field` from `vex-snippets.vfl`. Name it `wr_height`.
      Confirm `@height` shows up on the Points tab of the spreadsheet,
      with values roughly in `[-1.0, 1.0]`.
- [ ] **4. Append an Attribute Wrangle.** Run over: **Points**.
      Paste `vex_color_from_height` from `vex-snippets.vfl`. Name it `wr_color`.
      Confirm `@Cd` is present on points, three components, sane range.

## Phase 2 — Promotion / class change

- [ ] **5. Append an Attribute Promote.**
      Source: `height`, From: Point, To: Primitive, Promotion Method: **Average**.
      Name it `promote_pt_to_prim_avg`. Confirm `@height` now exists on the
      **Primitives** tab. Note: 400 point rows became 361 prim rows.
- [ ] **6. Append a second Attribute Promote.**
      Source: `height`, From: Primitive, To: Point, Promotion Method: **Maximum**.
      Name it `promote_prim_to_pt_max`. Confirm point `@height` now stair-steps
      at island borders compared to the original wrangle output.
- [ ] **7. Branch from `wr_color` directly into `OUT_data_view` (Null).**
      This is the "raw data" output.
- [ ] **8. Branch from `promote_prim_to_pt_max` into `OUT_render_ready` (Null).**
      This is the "promoted" output.

## Phase 3 — Proof capture

- [ ] **9. Capture proof.** Take the four screenshots described in
      `proof-template.md`. Fill in the four answers. Save `proof-template.md`
      with your answers and paste into Atlas /proof-packets.

## Failure modes to watch for

- "I changed Cd in a wrangle and the viewport didn't update" → almost always means
  the wrangle is not actually downstream of what the OUT is reading. Check the wires.
- "Attribute Promote is producing zeros" → the source attribute is missing on the
  expected class. Re-read the tab on the spreadsheet, not the network.
- "I don't see a Primitives tab" → your geometry has only points (e.g. a Scatter
  output). Add a Polygon-producing node or use the right output.
- "My @ptnum reordered when I deleted points" → @ptnum is a runtime index, not a
  stable id. If you need stability, add `i@id = @ptnum;` once before any deletion.
