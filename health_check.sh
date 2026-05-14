#!/bin/bash
# --- SETTINGS ---
TARGET="127.0.0.1"
STORAGE_PATH="/data"

echo "--- SYSTEM HEALTH CHECK ---"
date
echo "--- NETWORK STATUS ---"
ifconfig | grep "inet "
echo "--- STORAGE USAGE ---"
df -h $STORAGE_PATH | grep -v "Filesystem"
echo "--- SCANNING FOR OPEN PORTS ---"
nmap -F $TARGET | grep "open" || echo "No open ports found."
echo "--- CHECK COMPLETE ---"
