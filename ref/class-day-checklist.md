# Class day: student scans onto Explore

For a class where students scan an object with Scaniverse and see it on tanitxr.org/explore, in
the headset, a few minutes later. Settings: ref/class-drop.json. The code: tools/class_drop.py.

## The night before

1. Make sure the Drive folder in ref/class-drop.json is set to "Anyone with the link: Editor"
   (Share, then General access). Students upload to it signed in to any Google account.
   Test it yourself from your phone with a tiny file.
2. If Google Drive for desktop is installed and signed in to the account that owns the folder,
   add the folder's path on this laptop to "folders" in ref/class-drop.json. Then uploads arrive
   on the laptop by themselves. Without it, download each file from drive.google.com into
   Downloads, which is watched too: one click per scan.
3. Charge the headset and pair it with the room's Wi-Fi. Open tanitxr.org/explore in it once so
   the browser has the page cached.
4. On the laptop, one dry run:

       python3 tools/class_drop.py watch

   Drop any .glb into ~/ClassDrop and watch the log say "pushed". Then:

       python3 tools/class_drop.py remove-all

5. `npx` needs the internet the first time it runs gltf-transform on a laptop; after that it is
   cached. Run the dry run on the same laptop you will bring.

## In class

- Put tanitxr.org/drop on the screen. It has the three steps and the QR code.
- Start the watcher in a terminal and leave it running:

      python3 tools/class_drop.py watch

- Students: Scaniverse, Share, Export Model, GLB, name it FirstName_Object.glb, upload. iPhones can
  also AirDrop the file to you; it lands in Downloads and goes up by itself.
- A scan is live on tanitxr.org/explore about one minute after it reaches the laptop, in the room
  named in ref/class-drop.json at the end of the page. Reload the Explore page in the headset to see
  new ones. The watcher log says which name went up and when.
- If the room's internet is slow, the headset can read straight from the laptop. In a second
  terminal:

      python3 -m http.server 8737 --directory docs --bind 0.0.0.0

  and open http://LAPTOP-IP:8737/explore/ in the headset. The watcher prints the address when it
  starts. New scans show there within seconds, no GitHub needed.
- A file by hand, with the credit spelt out:

      python3 tools/class_drop.py add ~/Downloads/scan.glb --by Maya --title "Coffee mug"

## What can go wrong

- A scan that is too big (a huge object or Scaniverse on the highest detail): the watcher tries
  textures at 2048, 1024 and 512, then decimates the mesh in Blender. That takes about a minute
  and the result is lighter but still recognisable. If it fails the log says so and the file is
  skipped; the student can export again at lower detail.
- A file named without an underscore gets no name on the credit line. Rename it and drop it again,
  or use the add command with --by.
- Two students pick the same object name: the second one gets a -2 slug, both appear.
- The watcher stops if the laptop sleeps. Set the laptop not to sleep for the class.
- GitHub push fails (no internet): the log says "push failed". The scan is still on the laptop
  preview address above, and the next successful push carries everything so far.

## After

    python3 tools/class_drop.py list
    python3 tools/class_drop.py remove-all      # or leave them up as a student gallery

The originals stay where the students put them. Only the shrunk copies are on the site.
