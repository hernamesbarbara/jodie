#!/usr/bin/env bash
echo "Installing jodie with \`pyinstaller/install-jodie.sh\`"
echo

pyinstaller --name jodie --onefile jodie/__main__.py
echo "done"
echo

echo "Signing code with Apple entitlements for macOS Contacts..."
codesign \
    --entitlements jodie.entitlements \
    --sign "$APPLE_DEVELOPER_ID_APPLICATION" \
    --options runtime \
    --force \
    dist/jodie

# https://forums.developer.apple.com/forums/thread/86161
# codesign --remove-signature dist/jodie
# codesign -dv --verbose=4 dist/jodie
