# Curve Skeleton / Alien Limb — Build Checklist

## Phase 1 — Curve from data

- [ ] **1. Geometry SOP** named `geo_alien_limb`. Dive inside.
- [ ] **2. Table Import / File SOP** loading `points.csv`.
      Confirm: 8 points on the spreadsheet with `P`, `@id`, `@width`.
- [ ] **3. Add SOP** with **By Group: All Points → Polygon Open**.
      Confirm the Primitives tab shows 1 polyline of 8 vertices.
- [ ] **4. Resample SOP** to 64 segments along curve `U`. Maximum Segment
      Length 0 (segment count drives). Output **PointAttribs: P, N**.
- [ ] **5. Attribute Wrangle `wr_seg_id` (run over: Points)** —
      `vex_segment_id`. Confirm `@seg_id` runs 0..63.

## Phase 2 — Orient that survives a degenerate up

- [ ] **6. Attribute Wrangle `wr_orient` (run over: Points)** —
      `vex_robust_orient`. Confirm `@orient` is a 4-component quaternion
      attribute on every point and that `length(@orient)` ≈ 1.
- [ ] **7. Test:** parameter-sweep the up vector through `(0,1,0) → (0,0,1)`.
      Segments must NOT flip 180°. If they do, the snippet was pasted into
      the wrong wrangle or the up-vector came from a degenerate cross.

## Phase 3 — Segment geometry copied along curve

- [ ] **8. Tube SOP `seg_capsule`** (Capped, low-poly). Radius 0.05, Height 1.
      End Caps **Triangulated**. Center **Y**.
- [ ] **9. Attribute Wrangle `wr_width_scale` (run over: Points, on the resampled curve)** —
      `vex_segment_width`. Confirm `@pscale` exists per point.
- [ ] **10. Copy to Points** with capsule as input 1, resampled curve as
      input 2. **Pack and Instance**: off (you want geometry first time).
      Confirm 64 capsule copies appear, oriented along the curve, scaled
      by `@pscale`.
- [ ] **11. Null `OUT_alien_limb`.** This is the limb output.

## Failure modes to watch for

- **Limb flips orientation** when you parameter-sweep the up vector.
  → Almost always `cross(tangent, up)` returning zero. Use the snippet
  `vex_robust_orient` exactly — it falls back to a different up axis when
  the cross product collapses.
- **Segments re-shuffle** when you change anything upstream.
  → You did not freeze a stable `@id`. Add `vex_segment_id` BEFORE any
  delete or filter.
- **CurveU vs ptnum confusion.** `@curveu` is a normalised 0..1 float
  along the curve. `@ptnum` is a runtime row index. They are not the same.
- **`@N` is missing on the resample output.** Resample only outputs N if
  you asked for it explicitly in the Output PointAttribs.
