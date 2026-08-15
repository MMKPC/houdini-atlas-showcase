# Houdini Atlas — Alien Spider Capstone planning pack
# HOM SCAFFOLD — REVIEW BEFORE RUN.
#
# This is a SCAFFOLD: it shows the subnet skeleton, not the contents.
# Building the legs subnet, the carapace subnet, and the controls null
# is the actual capstone work. Run this only if you understand it.

import hou

# --- Step 0 — parent ----------------------------------------------------
# parent = hou.node("/obj")
# geo = parent.node("geo_alien_spider") or parent.createNode("geo", "geo_alien_spider")

# --- Step 1 — top-level subnet ------------------------------------------
# spider = geo.node("subnet_alien_spider_v1") or geo.createNode("subnet", "subnet_alien_spider_v1")
# # Set 1 input + 2 outputs: spider.setInputs / hou.NetworkBox APIs differ across versions; verify.

# --- Step 2 — controls null (variation knobs) ---------------------------
# Inside spider:
# spider_inside = spider  # for clarity below
# controls = spider_inside.node("controls") or spider_inside.createNode("null", "controls")
# # Add spare parameters from variation-matrix.csv. The minimum required:
# #   leg_count (int 4-12, default 8)
# #   leg_segments (int 16-128, default 64)
# #   carapace_total_count (int 500-12000, default 4000)
# #   instance_count (int 1-32, default 4)
# #   instance_seed (int 1-9999, default 1)
# # Adding spare parameters via Python is verbose — most learners do this
# # in the parameter editor by hand. That is fine.

# --- Step 3 — legs subnet (consumes curve-skeleton-alien-limb pack) -----
# legs = spider_inside.node("legs") or spider_inside.createNode("subnet", "legs")
# # Inside `legs`, build a for-loop iterating leg_count times. Each iteration:
# #   - Loads / generates one leg curve (re-using the alien-limb network).
# #   - Sets i@leg_id = iteration.
# #   - Rotates around Y by (iteration / leg_count) * 360 deg.
# # Merge all iterations.

# --- Step 4 — carapace subnet (consumes scatter-surface-language pack) --
# carapace = spider_inside.node("carapace") or spider_inside.createNode("subnet", "carapace")
# # Inside `carapace`, the scatter pack network. The scatter result feeds
# # the instance_assignment wrangle.

# --- Step 5 — instance assignment ---------------------------------------
# inst = spider_inside.node("instance_assignment") or spider_inside.createNode("attribwrangle", "instance_assignment")
# inst.setInput(0, carapace)
# inst.parm("class").set(2)
# # Paste vex_instance_handoff into the snippet parm.

# --- Step 6 — merge + output --------------------------------------------
# merge = spider_inside.node("merge_skeleton") or spider_inside.createNode("merge", "merge_skeleton")
# merge.setInput(0, legs)
# merge.setInput(1, carapace)
# merge.setInput(2, inst)
# out = spider_inside.node("OUT_alien_spider_rest") or spider_inside.createNode("output", "OUT_alien_spider_rest")
# out.setInput(0, merge)


# ----------------------------------------------------------------------
# READ-ONLY VERIFICATION
# ----------------------------------------------------------------------
def verify():
    s = hou.node("/obj/geo_alien_spider/subnet_alien_spider_v1")
    if s is None:
        print("FAIL subnet missing"); return
    expected = ["controls", "legs", "carapace",
                "instance_assignment", "merge_skeleton", "OUT_alien_spider_rest"]
    missing = [n for n in expected if s.node(n) is None]
    if missing:
        print("FAIL missing:", missing); return
    out = s.node("OUT_alien_spider_rest")
    if out is None or out.geometry() is None:
        print("FAIL no geometry on OUT"); return
    g = out.geometry()
    leg_ids = set()
    for pt in g.points():
        try:
            leg_ids.add(pt.attribValue("leg_id"))
        except hou.OperationFailed:
            pass
    print(f"INFO distinct @leg_id values on OUT: {len(leg_ids)} (expect 8 if leg_count=8).")
    has_idx = any(a.name() == "instance_index" for a in g.pointAttribs())
    print("PASS" if has_idx else "FAIL", " - @instance_index present:", has_idx)

# Uncomment AFTER you have built the subnet:
# verify()
