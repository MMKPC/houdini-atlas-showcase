# Houdini Atlas — Scatter Surface Language starter pack
# HOM build plan — REVIEW BEFORE RUN.
#
# Every node creation and parameter set is COMMENTED. Read first.

import hou

# parent = hou.node("/obj")
# geo = parent.node("geo_scatter_surface") or parent.createNode("geo", "geo_scatter_surface")

# --- Sphere -------------------------------------------------------------
# sphere = geo.node("sphere") or geo.createNode("sphere", "sphere")
# sphere.parm("type").set(0)   # 0 = polygon
# sphere.parm("freq").set(60)  # parm name varies; verify

# --- Mountain -----------------------------------------------------------
# mountain = geo.node("mountain") or geo.createNode("mountain", "mountain")
# mountain.setInput(0, sphere)
# mountain.parm("amp").set(0.4)
# mountain.parm("elementsize").set(0.8)

# --- Recompute @N -------------------------------------------------------
# wr_n = geo.node("wr_recompute_N") or geo.createNode("attribwrangle", "wr_recompute_N")
# wr_n.setInput(0, mountain)
# wr_n.parm("class").set(2)
# # Paste vex_recompute_normals into wr_n's snippet parm.

# --- Density mask -------------------------------------------------------
# wr_mask = geo.node("wr_density_mask") or geo.createNode("attribwrangle", "wr_density_mask")
# wr_mask.setInput(0, wr_n)
# wr_mask.parm("class").set(2)
# # Choose a recipe from mask-recipes.json and paste the matching snippet.

# --- Visualise ----------------------------------------------------------
# wr_viz = geo.node("wr_visualise_mask") or geo.createNode("attribwrangle", "wr_visualise_mask")
# wr_viz.setInput(0, wr_mask)
# wr_viz.parm("class").set(2)
# wr_viz.parm("snippet").set("@Cd = set(@density_mask, @density_mask, @density_mask);\n")

# --- Scatter ------------------------------------------------------------
# scatter = geo.node("scatter") or geo.createNode("scatter", "scatter")
# scatter.setInput(0, wr_mask)
# # Parm names differ across versions. The two important ones:
# # scatter.parm("density").set(1)            # use density attribute
# # scatter.parm("densityattrib").set("density_mask")
# # scatter.parm("forcetotalcount").set(1)
# # scatter.parm("totalcount").set(4000)
# # scatter.parm("seed").set(1)

# --- Inspector ---------------------------------------------------------
# wr_insp = geo.node("wr_scatter_inspect") or geo.createNode("attribwrangle", "wr_scatter_inspect")
# wr_insp.setInput(0, scatter)
# wr_insp.parm("class").set(2)
# # Paste vex_scatter_inspect into wr_insp's snippet parm.

# --- OUT ---------------------------------------------------------------
# out = geo.node("OUT_scattered_surface") or geo.createNode("null", "OUT_scattered_surface")
# out.setInput(0, wr_insp)


# ----------------------------------------------------------------------
# READ-ONLY VERIFICATION — run after the network exists.
# ----------------------------------------------------------------------
def verify():
    geo = hou.node("/obj/geo_scatter_surface")
    if geo is None:
        print("FAIL geo missing"); return
    expected = ["sphere", "mountain", "wr_recompute_N", "wr_density_mask",
                "wr_visualise_mask", "scatter", "wr_scatter_inspect",
                "OUT_scattered_surface"]
    missing = [n for n in expected if geo.node(n) is None]
    if missing:
        print("FAIL missing:", missing); return
    g = geo.node("OUT_scattered_surface").geometry()
    print("INFO scatter output points:", len(g.points()), "(expect 4000)")
    has_neigh = any(a.name() == "neighbour_count" for a in g.pointAttribs())
    has_dens  = any(a.name() == "local_density_estimate" for a in g.pointAttribs())
    print("PASS" if has_neigh else "FAIL", " - @neighbour_count present:", has_neigh)
    print("PASS" if has_dens  else "FAIL", " - @local_density_estimate present:", has_dens)
    # mask sanity: density_mask should exist on the upstream wrangle output
    src = geo.node("wr_density_mask").geometry()
    has_mask = any(a.name() == "density_mask" for a in src.pointAttribs())
    print("PASS" if has_mask else "FAIL", " - @density_mask on points (NOT primitives):", has_mask)

# Uncomment to run AFTER you have built the network:
# verify()
