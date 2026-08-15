# Houdini Atlas — Curve Skeleton / Alien Limb starter pack
# HOM build plan — REVIEW BEFORE RUN.
#
# Every node creation and parameter set is COMMENTED. Read first. Uncomment
# the sections you understand. Building the network by hand is the lesson.
#
# Required side files (sit next to this script):
#   points.csv
#   vex-snippets.vfl

import hou

# --- Step 0 — locate or create the parent geometry SOP --------------------
# parent = hou.node("/obj")
# geo = parent.node("geo_alien_limb") or parent.createNode("geo", "geo_alien_limb")

# --- Step 1 — load CSV ----------------------------------------------------
# Load via Table Import (parm names differ across versions — verify).
# csv_import = geo.node("csv_import") or geo.createNode("tableimport", "csv_import")
# csv_import.parm("file").set("$HIP/points.csv")
# csv_import.parm("headerlines").set(1)

# --- Step 2 — connect points into one open polyline ------------------------
# add1 = geo.node("make_polyline") or geo.createNode("add", "make_polyline")
# add1.setInput(0, csv_import)
# # Switch to "By Group: All Points → Polygon Open"; parm name is "switcher" or
# # "addgroup" depending on version. Verify in your build.

# --- Step 3 — resample ---------------------------------------------------
# resample = geo.node("resample") or geo.createNode("resample", "resample")
# resample.setInput(0, add1)
# resample.parm("method").set(1)  # 1 = By Number Of Segments on most builds
# resample.parm("segs").set(64)
# resample.parm("dotang").set(1)  # output @N
# resample.parm("docurveu").set(1)

# --- Step 4 — Wrangle: stable @seg_id ------------------------------------
# wr_seg = geo.node("wr_seg_id") or geo.createNode("attribwrangle", "wr_seg_id")
# wr_seg.setInput(0, resample)
# wr_seg.parm("class").set(2)  # 2 = Points
# wr_seg.parm("snippet").set("i@seg_id = @ptnum;\n")

# --- Step 5 — Wrangle: robust @orient ------------------------------------
# wr_or = geo.node("wr_orient") or geo.createNode("attribwrangle", "wr_orient")
# wr_or.setInput(0, wr_seg)
# wr_or.parm("class").set(2)
# # Open vex-snippets.vfl, copy "vex_robust_orient" body into the snippet parm.
# # We do NOT inline the snippet here so the canonical source stays in one place.

# --- Step 6 — Wrangle: @pscale -------------------------------------------
# wr_w = geo.node("wr_width_scale") or geo.createNode("attribwrangle", "wr_width_scale")
# wr_w.setInput(0, wr_or)
# wr_w.parm("class").set(2)
# # Copy "vex_segment_width" body from vex-snippets.vfl.

# --- Step 7 — capsule + copy to points ------------------------------------
# tube = geo.node("seg_capsule") or geo.createNode("tube", "seg_capsule")
# tube.parm("type").set(0)    # polygon
# tube.parm("rad1").set(0.05)
# tube.parm("rad2").set(0.05)
# tube.parm("height").set(1.0)
# tube.parm("orient").set(1)  # Y axis
# c2p = geo.node("copy_to_points") or geo.createNode("copytopoints", "copy_to_points")
# c2p.setInput(0, tube)
# c2p.setInput(1, wr_w)

# --- Step 8 — OUT --------------------------------------------------------
# out = geo.node("OUT_alien_limb") or geo.createNode("null", "OUT_alien_limb")
# out.setInput(0, c2p)

# --------------------------------------------------------------------------
# READ-ONLY VERIFICATION — run after the network exists.
# --------------------------------------------------------------------------
def verify():
    geo = hou.node("/obj/geo_alien_limb")
    if geo is None:
        print("FAIL: /obj/geo_alien_limb missing.")
        return
    expected = ["csv_import", "make_polyline", "resample",
                "wr_seg_id", "wr_orient", "wr_width_scale",
                "seg_capsule", "copy_to_points", "OUT_alien_limb"]
    missing = [n for n in expected if geo.node(n) is None]
    if missing:
        print("FAIL missing:", missing); return
    g = geo.node("OUT_alien_limb").geometry()
    n_pts = len(g.points())
    print(f"INFO OUT_alien_limb total points (capsules x verts): {n_pts}")
    src = geo.node("wr_width_scale").geometry()
    print(f"INFO resampled curve has {len(src.points())} points (expect 64).")
    has_orient = any(a.name() == "orient" for a in src.pointAttribs())
    has_seg = any(a.name() == "seg_id" for a in src.pointAttribs())
    has_pscale = any(a.name() == "pscale" for a in src.pointAttribs())
    print("PASS" if has_orient else "FAIL", " - @orient on resampled curve:", has_orient)
    print("PASS" if has_seg else "FAIL",    " - @seg_id on resampled curve:", has_seg)
    print("PASS" if has_pscale else "FAIL", " - @pscale on resampled curve:", has_pscale)

# Uncomment to run AFTER you have built the network:
# verify()
