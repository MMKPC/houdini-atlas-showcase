# Houdini Atlas — SOP Data Foundations starter pack
# HOM (Houdini Object Model) BUILD PLAN — REVIEW BEFORE RUN.
#
# DO NOT BLINDLY EXECUTE THIS FILE. Every action that creates or modifies a
# node is intentionally COMMENTED OUT. Read the code, decide whether you
# want each line to run, then uncomment selectively.
#
# This file is a *plan*, not a tool. Building the network by hand inside
# Houdini is part of the lesson — using this file as auto-magic skips the
# learning. The included assertions are honest checks: they fail loudly if
# Houdini's data does not match what the lesson predicts.
#
# How to use:
#   1. Open Houdini.
#   2. Open the Python Source Editor (Windows > Python Source Editor).
#   3. Paste this file. READ IT. Comment status: every parm.set / hou.node()
#      mutating call is commented with a leading "#". Uncomment a section
#      only after you understand what it will do.
#   4. Optionally run the read-only assertions at the bottom AFTER you have
#      built the network manually — they verify your work, they do not
#      build it for you.

import hou  # Houdini's Python module — only available inside a Houdini session.

# ----------------------------------------------------------------------
# Step 0 — Locate (or create) the parent geometry SOP.
# ----------------------------------------------------------------------
# parent = hou.node("/obj")
# geo = parent.node("geo_sop_foundations") or parent.createNode("geo", "geo_sop_foundations")

# ----------------------------------------------------------------------
# Step 1 — Grid.
# ----------------------------------------------------------------------
# grid1 = geo.node("grid1") or geo.createNode("grid", "grid1")
# grid1.parm("rows").set(20)
# grid1.parm("cols").set(20)
# grid1.parm("sizex").set(10)
# grid1.parm("sizey").set(10)
# grid1.parm("orient").set(0)  # 0 = ZX in many Houdini versions; verify on your build

# ----------------------------------------------------------------------
# Step 2 — Attribute Wrangle: wr_height.
# ----------------------------------------------------------------------
# wr_height = geo.node("wr_height") or geo.createNode("attribwrangle", "wr_height")
# wr_height.setInput(0, grid1)
# wr_height.parm("class").set(2)  # 0=detail, 1=primitive, 2=point, 3=vertex on most builds
# wr_height.parm("snippet").set(
#     "vector p = @P;\n"
#     "float n = noise(p * 0.35);\n"
#     "@height = fit01(n, -1.0, 1.0);\n"
# )

# ----------------------------------------------------------------------
# Step 3 — Attribute Wrangle: wr_color.
# ----------------------------------------------------------------------
# wr_color = geo.node("wr_color") or geo.createNode("attribwrangle", "wr_color")
# wr_color.setInput(0, wr_height)
# wr_color.parm("class").set(2)
# wr_color.parm("snippet").set(
#     "float h01 = fit(@height, -1.0, 1.0, 0.0, 1.0);\n"
#     "@Cd = set(h01, h01 * 0.6, 1.0 - h01);\n"
# )

# ----------------------------------------------------------------------
# Step 4 — Attribute Promote: pt -> prim, average.
# ----------------------------------------------------------------------
# p1 = geo.node("promote_pt_to_prim_avg") or geo.createNode("attribpromote", "promote_pt_to_prim_avg")
# p1.setInput(0, wr_color)
# p1.parm("inname").set("height")
# # parm names below differ across Houdini versions — VERIFY IN YOUR BUILD before uncommenting.
# # p1.parm("inclass").set(0)   # 0 = Point in some versions
# # p1.parm("outclass").set(1)  # 1 = Primitive
# # p1.parm("method").set(0)    # 0 = Average

# ----------------------------------------------------------------------
# Step 5 — Attribute Promote: prim -> pt, maximum.
# ----------------------------------------------------------------------
# p2 = geo.node("promote_prim_to_pt_max") or geo.createNode("attribpromote", "promote_prim_to_pt_max")
# p2.setInput(0, p1)
# p2.parm("inname").set("height")
# # p2.parm("inclass").set(1)   # 1 = Primitive
# # p2.parm("outclass").set(0)  # 0 = Point
# # p2.parm("method").set(2)    # 2 = Maximum (verify on your build)

# ----------------------------------------------------------------------
# Step 6 — Two named OUTs.
# ----------------------------------------------------------------------
# out_data_view = geo.node("OUT_data_view") or geo.createNode("null", "OUT_data_view")
# out_data_view.setInput(0, wr_color)
# out_render_ready = geo.node("OUT_render_ready") or geo.createNode("null", "OUT_render_ready")
# out_render_ready.setInput(0, p2)

# ----------------------------------------------------------------------
# READ-ONLY VERIFICATION — safe to run once the network exists.
# These assertions DO NOT modify the scene. They just print PASS / FAIL.
# ----------------------------------------------------------------------
def verify():
    geo = hou.node("/obj/geo_sop_foundations")
    if geo is None:
        print("FAIL: /obj/geo_sop_foundations does not exist yet.")
        return
    expected = ["grid1", "wr_height", "wr_color",
                "promote_pt_to_prim_avg", "promote_prim_to_pt_max",
                "OUT_data_view", "OUT_render_ready"]
    missing = [n for n in expected if geo.node(n) is None]
    if missing:
        print("FAIL: missing nodes:", missing)
        return
    out = geo.node("OUT_render_ready")
    geom = out.geometry()
    pts = len(geom.points())
    prims = len(geom.prims())
    print(f"INFO: OUT_render_ready has {pts} points, {prims} primitives.")
    print("EXPECT: 400 points, 361 primitives if the grid was 20x20.")
    has_height = any(a.name() == "height" for a in geom.pointAttribs())
    has_cd = any(a.name() == "Cd" for a in geom.pointAttribs())
    print("PASS" if has_height else "FAIL", " - point @height present:", has_height)
    print("PASS" if has_cd else "FAIL", " - point @Cd present:", has_cd)

# Uncomment to run verification AFTER you have built the network:
# verify()
