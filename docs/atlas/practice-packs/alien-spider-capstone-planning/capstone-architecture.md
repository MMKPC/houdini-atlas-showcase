# Capstone Architecture — Alien Spider

> Fill this in **before** you build. Treat it as a contract with your
> future self. If you cannot answer a row in one line, the build is not
> ready to start.

## 1 — Identity

- Capstone variation name (your choice):
- Date planned:
- Houdini version target:
- Estimated build time:

## 2 — Primary outputs

- One single packed-disk USD or BGEO of: ☐ rest pose ☐ animated pose
- Resolution target (poly count): from ☐ 250k ☐ 500k ☐ 1M ☐ other
- Render target: ☐ Karma CPU ☐ Karma XPU ☐ Mantra ☐ none (geometry only)

## 3 — Leg architecture

- How many legs: 8 (default — keep this)
- Leg curve source: imported from the **Curve Skeleton / Alien Limb pack**
  with N segments per leg = ____ (default: 64)
- Per-leg variation strategy:
  - ☐ Identical, mirrored only (cheap, brittle)
  - ☐ Per-leg seed offset (recommended)
  - ☐ Per-leg curve resample with shared id but different curl
- Stable id strategy (which attribute carries leg id?): `@leg_id` on
  every point of every leg. If you cannot point at it on the spreadsheet,
  the rig will scramble downstream.

## 4 — Carapace architecture

- Carapace surface source: from the **Scatter Surface Language pack** with
  - Recipe: ☐ rim ☐ dual_noise ☐ distance_from_curve ☐ combination
  - Mask combinator (if combination): see `vex-snippets.vfl` → `vex_mask_combinator`
- Plate geometry instanced on scatter: ☐ rivet ☐ plate ☐ pustule
  ☐ multiple via `@instance_index`
- Force Total Count target: ____ (default 4000)

## 5 — Cross-module composition

- Top-level subnet name: `subnet_alien_spider_v1`
- Number of inputs the subnet takes: ☐ 0 ☐ 1 (a control curve) ☐ 2
- Outputs the subnet exposes: ☐ rest pose only ☐ rest + simulation cache
- Variation knobs surfaced as spare parameters on this subnet:
  see `variation-matrix.csv`. Knobs marked **REQUIRED** must be exposed.

## 6 — Failure modes you will explicitly test

- ☐ Limb flips on degenerate up vector (test: parameter-sweep up axis).
- ☐ Scatter ignores mask (test: scatter point count vs mask sum).
- ☐ `@leg_id` re-shuffles when one leg curve is deleted upstream.
- ☐ `@instance_index` out-of-range when scatter density spikes.
- ☐ Scene non-determinism: same seed → different output across sessions.

## 7 — Proof artefacts you owe

See `proof-contract.md`. Tick which proof packet id each artefact will
flow into:

- Architecture screenshot → `proof.spider_architecture`
- Leg orient sweep → `proof.spider_legs_orient_stable`
- Carapace mask + scatter overlay → `proof.spider_carapace_mask`
- Variation matrix render (3 variations side by side) → `proof.spider_variations`
- Spreadsheet @leg_id integrity → `proof.spider_leg_id_integrity`
- Spreadsheet @instance_index sanity → `proof.spider_instance_index`
- Determinism check (same-seed re-run, byte match) → `proof.spider_determinism`
- Capstone readiness self-assessment → `proof.spider_self_review`

## 8 — Honesty

- What I am intentionally NOT doing in this capstone (so I can finish):
- What might break that I will accept and document instead of fixing:
- Stretch goal if I have time after the proofs:
