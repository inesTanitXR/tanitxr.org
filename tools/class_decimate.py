# Runs inside Blender, headless, for tools/class_drop.py when gltf-transform alone cannot get a
# scan under the page budget: a Scaniverse or Sketchfab mesh with millions of triangles. The
# meshopt simplifier stops at texture seams on such a mesh; Blender's Decimate does not.
#
#   /Applications/Blender.app/Contents/MacOS/Blender -b --python tools/class_decimate.py -- IN.glb OUT.glb RATIO
#
# Normals are not exported so the next gltf-transform pass can weld and compress what is left.
import sys

import bpy

argv = sys.argv[sys.argv.index("--") + 1:]
src, dst, ratio = argv[0], argv[1], float(argv[2])

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=src)
for ob in list(bpy.context.scene.objects):
    if ob.type != "MESH":
        continue
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    if len(ob.data.polygons) < 2000:
        continue
    m = ob.modifiers.new("dec", "DECIMATE")
    m.ratio = ratio
    m.use_collapse_triangulate = True
    bpy.ops.object.modifier_apply(modifier=m.name)
bpy.ops.export_scene.gltf(filepath=dst, export_format="GLB", export_normals=False,
                          export_apply=True, export_image_format="AUTO", export_yup=True)
