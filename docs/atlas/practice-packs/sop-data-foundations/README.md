# SOP Data Foundations Starter Pack

> Houdini Atlas — Module 1 (SOP Data Foundations) practice pack.
> Estimated time to complete: **45–75 minutes** in Houdini.
> You will build the Houdini scene yourself from these starter materials.

---

## What this pack is

A set of **starter materials** for the Houdini Atlas SOP Data Foundations module.
This pack does **not** include a `.hip` file. You build the file yourself in
your own copy of Houdini using the node plan, attribute manifest, checklist,
and VEX snippets included here. The point of the module is to *read SOP
networks as data tables* — so the proof you produce is a screenshot of the
Geometry Spreadsheet alongside your viewport, not a downloaded scene.

## What this pack is NOT

- **Not a `.hip` file.** The Atlas does not ship binary Houdini files.
- **Not a SideFX asset.** Nothing here is from SideFX. The included files are
  original educational material written for this curriculum.
- **Not auto-runnable.** The included `houdini-build-plan.py` is a HOM-style
  *review-before-run* outline. It is not wired up to execute on import. You
  paste it into the Houdini Python Source Editor only after you have read it.
- **Not a graded asset.** Your proof is the screenshots + spreadsheet rows,
  not a file the Atlas validates.

## Files in this pack

| File | Purpose |
| --- | --- |
| `README.md`              | This file. |
| `checklist.md`           | The 9-step build checklist you tick off in Houdini. |
| `node-plan.json`         | Machine-readable node graph plan (parents, names, parameters of interest). |
| `attribute-manifest.csv` | The attributes you should be able to point to on the spreadsheet. |
| `vex-snippets.vfl`       | Three small VEX snippets you paste into Attribute Wrangle nodes. |
| `houdini-build-plan.py`  | Commented HOM outline. **Review before run.** Does not auto-execute. |
| `proof-template.md`      | The proof-packet template you fill in once you finish. |
| `LICENSE.md`             | Educational use license note. |

## Linked module + lessons

- Module: **SOP Data Foundations** (Houdini Atlas Module 1)
- Lessons: `lesson.sop_mental_model`, `lesson.groups_masks_selection`
- Demos: `demo.sop_table_in_18`, `demo.noise_is_a_control_16`
- Assessment: `assess.sop_modeling_checkpoint`

## What you will build (concretely)

A small SOP network on a 20×20 grid that:

1. Reads a grid as **points + primitives** and lets you point to both on the spreadsheet.
2. Adds a per-point attribute via Attribute Wrangle (`@Cd`, `@height`).
3. Promotes it to primitive, then back to point with explicit averaging.
4. Has **two named OUT nodes** (`OUT_data_view`, `OUT_render_ready`).

## What you will prove (concretely)

Open the Geometry Spreadsheet and answer all four:

- Which row count appears under Points vs Primitives, and why are they different?
- After Attribute Promote (point→prim, average), which prims now have a smoothed `@height`?
- After Attribute Promote (prim→point, max), which points show a stair-step at island borders?
- Which class is `@ptnum` meaningful in, and which class is `@primnum` meaningful in?

If you cannot point at the rows on the spreadsheet, the module is not done.

## How to use this pack

1. Read `checklist.md` end to end before opening Houdini.
2. Open Houdini and create a new geometry SOP. Build the network from
   `node-plan.json` by hand. Do not paste `houdini-build-plan.py` until step 3.
3. Optional: paste `houdini-build-plan.py` into the Python Source Editor *to read it*.
   It is commented `# REVIEW BEFORE RUN`. Uncomment lines only if you understand them.
4. Use `vex-snippets.vfl` to fill in the wrangles named in `node-plan.json`.
5. Take the four screenshots described in `proof-template.md`.
6. Paste your filled-in `proof-template.md` into the Atlas under
   `/proof-packets` for the `demo.sop_table_in_18` session.

## Honesty

Houdini is large software with many supported versions. The node names and
parameter names in this pack are written for a recent Houdini 19.5/20.0 SOP
network and should be cross-checked against your local install. If a parameter
name has changed in your version, treat that as part of the learning, not an
error in the pack.
