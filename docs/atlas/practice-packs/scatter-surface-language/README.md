# Scatter Surface Language Starter Pack

> Houdini Atlas — Module 3 (Scatter and Surface Language) practice pack.
> Estimated time to complete: **60–90 minutes** in Houdini.
> You will build the Houdini scene yourself from these starter materials.

---

## What this pack is

A starter pack for learning **scatter as a language for surfaces** — not
as a magic button. You will build a network where:

- A **mask attribute** (point density, not boolean) drives scatter density.
- The mask is a *promoted* attribute, not a paint.
- A clear separation is enforced between **mask input class** (point) and
  **scatter input class** (primitive).
- Scatter output attributes are inspected on the spreadsheet for
  reproducibility — you can re-run with the same seed and get identical
  rows.

## What this pack is NOT

- **Not a `.hip` file.** No binary Houdini scene is shipped.
- **Not a SideFX asset.** No SideFX content used or referenced.
- **Not auto-runnable.** `houdini-build-plan.py` is a commented HOM
  outline — review before run.
- **Not a final scattering aesthetic.** This pack teaches the *language*.
  The aesthetic is a learner choice.

## Files in this pack

| File | Purpose |
| --- | --- |
| `README.md`             | This file. |
| `checklist.md`          | The 10-step build checklist. |
| `node-plan.json`        | Node graph plan with names, inputs, parameters of interest. |
| `mask-recipes.json`     | Three masking recipes (rim, dual-noise, distance-from-curve). |
| `vex-snippets.vfl`      | Three VEX snippets — rim mask, dual-noise mask, scatter inspector. |
| `houdini-build-plan.py` | Commented HOM build plan. **Review before run.** |
| `proof-template.md`     | Proof packet template. |
| `LICENSE.md`            | Educational use license note. |

## Linked module + lessons

- Module: **Scatter and Surface Language** (Houdini Atlas Module 3)
- Lessons: `lesson.scatter_as_language`, `lesson.masks_and_density`
- Demos: `demo.mask_scatter_22`, `demo.points_to_polys_and_back_11`
- Scenarios: `scenario.spider_carapace_scatter`
- Assessment: `assess.scatter_checkpoint`

## What you will build

1. A noisy displaced sphere as the surface input (consistent for everyone).
2. A point-class mask attribute (`@density_mask`) computed from a chosen
   masking recipe (rim / dual-noise / distance-from-curve).
3. A **Scatter SOP** that reads `@density_mask` from a point-class input
   (the failure mode this module fixes is feeding a primitive-class mask
   here without realising).
4. A diagnostic wrangle that writes per-scatter `@neighbour_count` and
   `@local_density_estimate` so the spreadsheet *proves* scatter is doing
   what you asked.

## What you will prove

- Scatter density visibly tracks the mask: rim recipe gives a corona,
  dual-noise gives clusters, distance-from-curve gives a gradient.
- Same Force Total Count + same seed = identical scatter coordinates
  (verify on the spreadsheet — a row count check is not enough).
- The diagnostic wrangle shows local density correlates with the mask
  value (R² visually obvious, no need to compute one).

## How to use this pack

1. Read `checklist.md`.
2. Build the network from `node-plan.json` by hand inside Houdini.
3. Pick a recipe from `mask-recipes.json` and paste the matching VEX from
   `vex-snippets.vfl`.
4. Optional: open `houdini-build-plan.py` in Python Source Editor and read
   it. Mutating calls are commented `# REVIEW BEFORE RUN`.
5. Capture proof per `proof-template.md` and save into Atlas /proof-packets
   for `demo.mask_scatter_22`.
