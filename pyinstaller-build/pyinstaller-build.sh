#!/usr/bin/env bash

echo "Running pyinstaller..."
pyinstaller --name jodie --onefile jodie/__main__.py
echo "done"
echo 

echo "Signing code with Apple entitlements for macOS Contacts..."
codesign \
    --entitlements jodie.entitlements \
    --sign "$APPLE_DEVELOPER_ID_APPLICATION" \
    --options runtime \
    dist/jodie

echo "done"
echo 

echo "Temporary work files, .log, .pyz and etc. in: ./build/"
echo "bundled app to ./dist/"
echo 
echo "done. exit(0)"
echo
