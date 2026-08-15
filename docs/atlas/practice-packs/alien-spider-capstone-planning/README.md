# Alien Spider Capstone Planning Pack

> Houdini Atlas — Module 7 (Procedural Alien Spider Capstone) planning pack.
> Estimated time to plan: **30–45 minutes**.
> Estimated build time, after planning: **6–12 hours** in Houdini.

---

## What this pack is

A **planning kit**, not a build kit. Before you spend 10 hours on the
capstone, you commit a one-page architecture: which modules contribute,
what attributes flow between them, what your variation knobs are, how
many proof rows you owe, and which failure modes you will check.

This pack ships:

- A capstone architecture template (markdown).
- A variation matrix CSV — eight knobs with default + min/max ranges.
- A proof contract listing the exact eight artefacts your capstone must produce.
- A network architecture JSON describing how the four prior modules
  (SOP foundations, curve skeleton, scatter, VEX) compose into a single
  scene.
- A handful of VEX snippets for the capstone-specific work (per-leg id
  stability, mask combinator, scatter-to-instance handoff).
- A commented HOM scaffold plan — review before run.

## What this pack is NOT

- **Not a `.hip` file.** No binary scene shipped — you build the scene
  from this plan plus the previous three packs (SOP foundations, curve
  skeleton, scatter). The capstone is the demonstration that you can
  *compose* the prior modules.
- **Not a SideFX asset.**
- **Not auto-runnable.** `houdini-build-plan.py` is a commented HOM
  scaffold — review before run.
- **Not a creature design.** The aesthetic of "what does this alien spider
  look like" is your choice. The pack ensures the *procedural plumbing*
  is honest.

## Files in this pack

| File | Purpose |
| --- | --- |
| `README.md`                | This file. |
| `capstone-architecture.md` | The one-page architecture you fill in BEFORE building. |
| `variation-matrix.csv`     | Eight variation knobs with default + range + which module owns them. |
| `proof-contract.md`        | The eight artefacts your capstone must produce. |
| `network-architecture.json`| Cross-module composition plan (which packs feed which). |
| `vex-snippets.vfl`         | Capstone-specific VEX (per-leg id, mask combinator, instance handoff). |
| `houdini-build-plan.py`    | Commented HOM scaffold. **Review before run.** |
| `LICENSE.md`               | Educational use license note. |

## Linked module + lessons

- Module: **Procedural Alien Spider Capstone** (Houdini Atlas Module 7)
- Prior modules required:
  - SOP Data Foundations (Module 1) — plus the matching pack.
  - Curve Skeleton Systems (Module 2) — plus the matching pack.
  - Scatter and Surface Language (Module 3) — plus the matching pack.
  - VEX as Control (Module 4) — review only.
  - Solver Basics (Module 5) — only if you choose to animate.
- Lessons: `lesson.capstone_setup`, `lesson.cross_module_composition`
- Demos: `demo.spider_carapace_v1_57`, `demo.spider_eight_legs_assembly_61`
- Scenarios: `scenario.alien_spider_creature_kit`
- Assessment: `assess.capstone_readiness_review`

## How to use this pack (the planning process)

1. **Open `capstone-architecture.md`.** Fill it in, end to end, before
   touching Houdini. Your future self will thank you. ~30 min.
2. **Pick variation knob defaults** from `variation-matrix.csv`. Lock in
   which knobs become spare parameters on a top-level `controls` Null.
3. **Read `network-architecture.json`** to confirm you understand the
   data flow: limb pack → 8 leg curves → carapace surface → scatter mask
   → instance handoff.
4. **Check `proof-contract.md`** — these are the eight artefacts you owe.
   Decide which ones map to which proof packet ids in the Atlas.
5. **Build in Houdini** using the prior packs as section references.
   The included `houdini-build-plan.py` is a *scaffold*: it shows the
   subnet structure, not the contents.
6. **Capture all 8 proofs.** Save against `demo.spider_eight_legs_assembly_61`.
