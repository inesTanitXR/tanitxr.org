// Writes a plain copy of a GLB: meshopt and Draco compression removed, so Blender can read it
// (tools/class_decimate.py). Run by tools/class_drop.py with the gltf-transform packages that
// npx already cached for the optimize step:
//   node tools/class_plain.cjs <node_modules dir> IN.glb OUT.glb
const [nm, src, dst] = process.argv.slice(2);
const { createRequire } = require('module');
const req = createRequire(nm.replace(/\/?$/, '/'));
const { NodeIO } = req('@gltf-transform/core');
const { ALL_EXTENSIONS } = req('@gltf-transform/extensions');
const { MeshoptDecoder } = req('meshoptimizer');
const draco = req('draco3dgltf');
(async () => {
  await MeshoptDecoder.ready;
  const io = new NodeIO().registerExtensions(ALL_EXTENSIONS)
    .registerDependencies({ 'meshopt.decoder': MeshoptDecoder, 'draco3d.decoder': await draco.createDecoderModule() });
  const doc = await io.read(src);
  for (const ext of doc.getRoot().listExtensionsUsed())
    if (['EXT_meshopt_compression', 'KHR_draco_mesh_compression'].includes(ext.extensionName)) ext.dispose();
  await io.write(dst, doc);
})().catch(e => { console.error(e.message || e); process.exit(1); });
