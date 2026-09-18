#!/usr/bin/env python3
"""Turn the volunteer-built pieces in the Unity museum project into web-ready glb files.

Usage:  python3 tools/convert_unity_pieces.py [/path/to/VRApp]

Needs Blender (found in /Applications) and node. For each piece in ref/made-pieces.json:
import the FBX, attach the textures the Unity materials point at (the FBX files themselves
carry none), export glb, then compress with gltf-transform (meshopt + webp). Output goes to
media/models/<slug>.glb plus a thumbnail in media/thumbs/<slug>.png; build.py ships both.
"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VRAPP = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Documents/GitHub/VRApp")
BLENDER = "/Applications/Blender.app/Contents/MacOS/Blender"
pieces = json.load(open(os.path.join(HERE, "ref", "made-pieces.json")))["pieces"]
out_dir = os.path.join(HERE, "media", "models")
os.makedirs(out_dir, exist_ok=True)

BLEND = r'''
import bpy, sys, os, json
args = sys.argv[sys.argv.index('--') + 1:]
root, plan, out = args[0], json.load(open(args[1])), args[2]
T = os.path.join(root, 'Assets/Textures/TileableTextures')
M = os.path.join(root, 'Assets/Models/TanitMuseum/TanitMuseumMainArea')
# material name prefix -> (base colour, normal map), read off the Unity .mat files
TEX = {
 'TanitMuseumMainArea_mat_01': (M + '/Tanit_OutDoorStructures_For_Texturing_02_TanitMuseumMainArea_mat_01_AlbedoTransparency.png', M + '/Tanit_OutDoorStructures_For_Texturing_02_TanitMuseumMainArea_mat_01_Normal.png'),
 'TanitMuseumMainArea_mat_02': (M + '/TanitMuseumMainSection_02_TanitMuseumMainArea_mat_02_AlbedoTransparency.png', M + '/TanitMuseumMainSection_02_TanitMuseumMainArea_mat_02_Normal.png'),
 'TanitMuseumMainArea_mat_03': (M + '/TanitMuseumMainArea_Texturing_Section_03_TanitMuseumMainArea_mat_03_AlbedoTransparency.png', M + '/TanitMuseumMainArea_Texturing_Section_03_TanitMuseumMainArea_mat_03_Normal.png'),
 'TanitMuseumMainArea_mat_04': (M + '/TanitMuseumMainArea_Texturing_Section_04_TanitMuseumMainArea_mat_04_AlbedoTransparency.png', M + '/TanitMuseumMainArea_Texturing_Section_04_TanitMuseumMainArea_mat_04_Normal.png'),
 'TanitMuseumMainArea_mat_05': (T + '/TilingPlane_Palm_Leaves_AlbedoTransparency.png', T + '/TilingPlane_Palm_Leaves_Normal.png'),
 'TanitMuseumMainArea_mat_floor_01': (T + '/SmoothStoneTiles_AlbedoTransparency.png', T + '/SmoothStoneTiles_Normal.png'),
 'TanitMuseumFountains_V04:M_TileTrimsheet1': (T + '/M_TileTrimsheet_BC.png', T + '/M_TileTrimsheet_NRM.png'),
 'standardSurface1': (T + '/M_TileTrimsheet_BC.png', T + '/M_TileTrimsheet_NRM.png'),
 'lambert1': (T + '/Tanit_Wall_01_Filler_BaseColor.1001.png', T + '/Tanit_Wall_01_Filler_Normal.1001.png'),
 'main_body': (os.path.join(root, 'Assets/Textures/stainedLamp/Tanit_opt_albedo.tga'), None),
}
def texture(mat):
    key = next((k for k in TEX if mat.name.startswith(k)), None)
    if not key: return
    base, nrm = TEX[key]
    if not os.path.exists(base): return
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = next((n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED'), None)
    if not bsdf: return
    if not bsdf.inputs['Base Color'].is_linked:
        img = nt.nodes.new('ShaderNodeTexImage'); img.image = bpy.data.images.load(base)
        nt.links.new(img.outputs['Color'], bsdf.inputs['Base Color'])
    if nrm and os.path.exists(nrm) and not bsdf.inputs['Normal'].is_linked:
        ni = nt.nodes.new('ShaderNodeTexImage'); ni.image = bpy.data.images.load(nrm)
        ni.image.colorspace_settings.name = 'Non-Color'
        nm = nt.nodes.new('ShaderNodeNormalMap')
        nt.links.new(ni.outputs['Color'], nm.inputs['Color']); nt.links.new(nm.outputs['Normal'], bsdf.inputs['Normal'])
    bsdf.inputs['Roughness'].default_value = 0.75
for p in plan:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=os.path.join(root, p['fbx']))
    for o in bpy.data.objects:
        if o.type == 'MESH':
            for m in o.data.materials:
                if m: texture(m)
    bpy.ops.export_scene.gltf(filepath=os.path.join(out, p['slug'] + '.glb'), export_format='GLB',
                              export_apply=True, export_yup=True)
    # a thumbnail for the map strip and share cards: three-quarter view, textured, no background
    import mathutils
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    pts = [o.matrix_world @ mathutils.Vector(c) for o in meshes for c in o.bound_box]
    mn = mathutils.Vector([min(q[i] for q in pts) for i in range(3)])
    mx = mathutils.Vector([max(q[i] for q in pts) for i in range(3)])
    center = (mn + mx) / 2; size = max(mx - mn) or 1
    sc = bpy.context.scene
    cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); sc.collection.objects.link(cam)
    sc.camera = cam; cam.data.lens = 45; cam.data.clip_end = size * 20
    d = size * 2.0
    cam.location = center + mathutils.Vector((d * 0.62, -d * 0.72, d * 0.42))
    cam.rotation_euler = (center - cam.location).to_track_quat('-Z', 'Y').to_euler()
    sc.render.engine = 'BLENDER_WORKBENCH'
    sc.display.shading.light = 'STUDIO'; sc.display.shading.color_type = 'TEXTURE'
    sc.display.shading.show_shadows = False; sc.display.shading.show_cavity = True
    sc.render.film_transparent = True
    sc.render.resolution_x = sc.render.resolution_y = 520; sc.render.resolution_percentage = 100
    sc.render.image_settings.file_format = 'PNG'; sc.render.image_settings.color_mode = 'RGBA'
    sc.render.filepath = os.path.join(args[3], p['slug'] + '.png')
    bpy.ops.render.render(write_still=True)
'''
with tempfile.TemporaryDirectory() as tmp:
    script = os.path.join(tmp, "blend.py"); open(script, "w").write(BLEND)
    plan = os.path.join(tmp, "plan.json"); json.dump(pieces, open(plan, "w"))
    raw = os.path.join(tmp, "raw"); os.makedirs(raw)
    thumbs = os.path.join(HERE, "media", "thumbs"); os.makedirs(thumbs, exist_ok=True)
    r = subprocess.run([BLENDER, "--background", "--python", script, "--", VRAPP, plan, raw, thumbs],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout[-2000:] + r.stderr[-2000:])
    for p in pieces:
        src = os.path.join(raw, p["slug"] + ".glb"); dst = os.path.join(out_dir, p["slug"] + ".glb")
        subprocess.run(["npx", "--yes", "@gltf-transform/cli@4", "optimize", src, dst, "--compress", "meshopt",
                        "--texture-compress", "webp", "--texture-size", "2048"], check=True, capture_output=True)
        print(f"{os.path.getsize(dst)/1e6:5.2f} MB  {p['slug']}")
