#!/bin/sh
# Renders flyer.html to a print PDF and a 2x PNG with headless Chrome.
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 \
  --print-to-pdf=elissa-flyer.pdf "file://$PWD/flyer.html" 2>/dev/null
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=8000 \
  --window-size=816,1056 --force-device-scale-factor=2 \
  --screenshot=elissa-flyer.png "file://$PWD/flyer.html" 2>/dev/null
