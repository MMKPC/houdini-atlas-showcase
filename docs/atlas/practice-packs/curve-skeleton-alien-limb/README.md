# Curve Skeleton / Alien Limb Starter Pack

> Houdini Atlas — Module 2 (Curve Skeleton Systems) practice pack.
> Estimated time to complete: **75–120 minutes** in Houdini.
> You will build the Houdini scene yourself from these starter materials.

---

## What this pack is

A starter pack for building a **single articulated alien limb** as a curve
skeleton. The output is one segmented limb you can copy/instance later for
the Alien Spider capstone. The pack ships:

- A node plan you build by hand inside Houdini.
- A `points.csv` of explicit control points so the same curve appears for
  every learner — same proof, different builds.
- VEX snippets that compute `@orient` and `@N` correctly *even on
  degenerate up vectors* (the most common limb-flip bug).
- A copy-to-points contract so segments cannot reorder when you re-time.

## What this pack is NOT

- **Not a `.hip` file.** No binary scene is shipped. You build the scene
  yourself from the included plan.
- **Not a SideFX asset.** No SideFX content is included or referenced.
- **Not auto-runnable.** `houdini-build-plan.py` is a commented HOM
  outline — review before run.
- **Not a rig.** No bones, no kinematics, no FBX. This is the *geometric
  skeleton* that drives later procedural alien spider work.

## Files in this pack

| File | Purpose |
| --- | --- |
| `README.md`             | This file. |
| `checklist.md`          | The 11-step build checklist. |
| `node-plan.json`        | Node graph plan (parents, names, parameters of interest). |
| `points.csv`            | 8 control points (P, @id, @width) defining a single limb curve. |
| `vex-snippets.vfl`      | Three VEX snippets: stable id, robust orient, segment width. |
| `houdini-build-plan.py` | Commented HOM build plan. **Review before run.** |
| `proof-template.md`     | Proof packet template. |
| `LICENSE.md`            | Educational use license note. |

## Linked module + lessons

- Module: **Curve Skeleton Systems** (Houdini Atlas Module 2)
- Lessons: `lesson.curves_as_skeletons`, `lesson.orient_and_normal_basics`
- Demos: `demo.curve_resample_orient_05`, `demo.copy_segments_along_curve_07`
- Scenarios: `scenario.alien_limb_v1`
- Assessment: `assess.curve_skeleton_checkpoint`

## What you will build

A single alien limb as a SOP network:

1. Eight control points loaded from `points.csv`.
2. Resampled curve at 64 segments with stable `@id` per segment.
3. A robust `@orient` per segment that does NOT flip when the curve passes
   through a degenerate up vector (the canonical bug this module fixes).
4. A segment "knuckle" capsule copied along the curve via Copy to Points,
   with `@width` driving non-uniform scale.

## What you will prove

- Toggle the up-vector source between two values; the segments must NOT
  flip orientation. Show a side-by-side capture.
- Delete one control point upstream; downstream segments must still
  reference the same `@id` they had before (no re-shuffle).
- Re-time the limb (parameter sweep on the resample length); the
  segment count and `@id` mapping must remain stable.

## How to use this pack

1. Read `checklist.md`.
2. In Houdini, build the network from `node-plan.json`. Use `points.csv`
   as a Table Import or as a CSV → Add SOP source.
3. Paste VEX snippets into the wrangles named in the plan.
4. Optional: open `houdini-build-plan.py` in Python Source Editor and read
   it. Do not auto-run — every mutating call is commented `# REVIEW BEFORE RUN`.
5. Capture the proof per `proof-template.md`.
6. Save the proof markdown into Atlas /proof-packets for
   `demo.copy_segments_along_curve_07`.
