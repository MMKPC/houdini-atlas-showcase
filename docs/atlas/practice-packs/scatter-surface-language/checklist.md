# Scatter Surface Language — Build Checklist

## Phase 1 — Surface input (consistent for everyone)

- [ ] **1. Geometry SOP** named `geo_scatter_surface`. Dive inside.
- [ ] **2. Sphere SOP** type Polygon, frequency 60. Append a **Mountain SOP**
      with `Amplitude 0.4`, `Element Size 0.8`. This is the surface.
      Confirm prim count > 6000.
- [ ] **3. Attribute Wrangle `wr_recompute_N` (Run over: Points)** —
      `vex_recompute_normals` from `vex-snippets.vfl`. Mountain can leave
      `@N` undefined on edges; recompute now.

## Phase 2 — Mask (point class!)

- [ ] **4. Decide a recipe** — see `mask-recipes.json`. Three options:
      `rim`, `dual_noise`, `distance_from_curve`.
- [ ] **5. Attribute Wrangle `wr_density_mask` (Run over: Points)** —
      paste the snippet matching your recipe. Confirm `@density_mask`
      is on the **Points** tab, not the Primitives tab. THIS IS THE BUG
      THIS MODULE FIXES — Scatter expects point-class density.
- [ ] **6. Visualise the mask.** Append an Attribute Wrangle:
      `@Cd = set(@density_mask, @density_mask, @density_mask);`
      Confirm the viewport shows the mask shape clearly.

## Phase 3 — Scatter

- [ ] **7. Scatter SOP** with **Force Total Count 4000**, seed `1`.
      Density attribute: `density_mask`. Geometry input: the masked surface.
      Confirm 4000 points appear, biased to high-mask regions.
- [ ] **8. Diagnostic wrangle `wr_scatter_inspect` (Run over: Points)** on
      the scatter output — `vex_scatter_inspect` from snippets. Adds
      `@neighbour_count` and `@local_density_estimate`.
- [ ] **9. Reproducibility check.** Press the seed up by 1, then back to 1.
      The spreadsheet rows must match the original byte-for-byte for the
      first 20 points. (If they do not, something upstream is non-deterministic.)
- [ ] **10. Null `OUT_scattered_surface`.** This is the output.

## Failure modes to watch for

- **Scatter ignores my mask completely.** Almost always means
  `@density_mask` is on the Primitives class (you wrote it in a wrangle
  set to Run over Primitives) and Scatter is reading nothing. Fix: write
  it on Points.
- **Scatter output is sparse where mask is bright.** You may have inverted
  the mask (low values = low density). Confirm range: min=0, max=1 is
  the convention; Scatter weights linearly.
- **Identical seed gives different output each session.** Almost always
  means an upstream node has time-dependent input (e.g. a Mountain SOP
  with `$F` in element seed). Freeze the source surface.
- **Mask leaks across an island border.** You probably promoted via
  `average` when you wanted `maximum` — promotion method matters.
