# Proof Contract — Alien Spider Capstone

The capstone is *not done* until all eight artefacts below are saved as
proof packets in Atlas under `demo.spider_eight_legs_assembly_61`.

| # | id | What it proves | How to capture |
|---|----|----------------|----------------|
| 1 | `proof.spider_architecture` | The subnet boundary is honest: one input curve, two outputs (rest, sim). | Network view screenshot of `subnet_alien_spider_v1` showing inputs + outputs labeled. |
| 2 | `proof.spider_legs_orient_stable` | Limbs do not flip on degenerate up vectors. | Two viewport screenshots: `up=(0,1,0)` and `up=(0,0,1)`. No 180° flips on any leg. |
| 3 | `proof.spider_carapace_mask` | Carapace scatter follows the chosen mask. | Side-by-side mask viz + scatter output viewport. |
| 4 | `proof.spider_variations` | Variation knobs actually drive variation. | Three rendered (or viewport) variations using three rows from `variation-matrix.csv`, side by side. |
| 5 | `proof.spider_leg_id_integrity` | `@leg_id` survives upstream edits. | Spreadsheet on the legs subnet output, after deleting one upstream control point. `@leg_id` distinct-value count must remain 8. |
| 6 | `proof.spider_instance_index` | `@instance_index` is in-range and stable across seeds. | Spreadsheet column min/max + a histogram-by-eyeball screenshot. |
| 7 | `proof.spider_determinism` | Same seed → identical output. | Two saves of the first 20 rows of the scatter output spreadsheet, run on different days, byte-identical. |
| 8 | `proof.spider_self_review` | Honest self-rating against the architecture you committed to in `capstone-architecture.md`. | One markdown — what you built, what you cut, what you would do next. |

## Honesty rules

- A blurry render screenshot does not satisfy any of the spreadsheet
  proofs (#5, #6). The spreadsheet is the source of truth for procedural
  proof — render it, do not eyeball it.
- "Looks fine" is not a pass. Every proof references either a spreadsheet
  row count, a column distinct-count, or an explicit before/after.
- If you cannot produce a proof, document *which one is missing and why*
  in `proof.spider_self_review`. The capstone allows up to 1 missing
  proof if the gap is named — never more.
