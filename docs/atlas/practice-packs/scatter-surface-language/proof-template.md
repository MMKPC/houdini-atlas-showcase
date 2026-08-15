# Proof Packet — Scatter Surface Language

> Fill in after building the scatter scene. Paste into Atlas /proof-packets
> for `demo.mask_scatter_22`.

## Identity

- Learner key: `default`
- Houdini version:
- Date:
- Recipe used: ☐ rim   ☐ dual_noise   ☐ distance_from_curve

## Screenshots (4 required)

1. **Network view.** sphere → mountain → wr_recompute_N → wr_density_mask →
   wr_visualise_mask → scatter → wr_scatter_inspect → OUT_scattered_surface.
   *File:* `01_network.png`

2. **Spreadsheet on `wr_density_mask`** — confirm `@density_mask` is on the
   **Points** tab (NOT the Primitives tab). This is the bug this module fixes.
   *File:* `02_mask_class_proof.png`

3. **Viewport at scatter output** — points clearly biased to high-mask regions.
   *File:* `03_viewport_scatter.png`

4. **Spreadsheet on `wr_scatter_inspect`** — `@neighbour_count` and
   `@local_density_estimate` columns visible, with high values where mask
   was bright, low where mask was dark.
   *File:* `04_inspect_proof.png`

## Three answers (1 line each)

1. *On which class is `@density_mask` defined? What would happen if you
   accidentally wrote it on the Primitives class instead?*

2. *Same seed, same Force Total Count — did the spreadsheet rows match
   exactly between two runs? If not, what upstream node was non-deterministic?*

3. *Why does the rim recipe require a recomputed `@N`? What did the
   spreadsheet show before recompute?*

## Failure log

- Did Scatter ignore your mask the first time? What was the actual cause?
- Did the seed sweep produce identical first-20 rows on a repeat?
- Did the viewport visualisation step catch a problem before Scatter ran?

## Self-rating (optional, learner-entered)

- Confidence I can apply this to a different surface: **___ / 5**
- Confidence I can debug "Scatter is ignoring my mask" elsewhere: **___ / 5**
