#!/bin/bash
echo "--- SYSTEM HEALTH CHECK ---"
date
echo "--- NETWORK STATUS ---"
ifconfig | grep "inet "
echo "--- STORAGE USAGE ---"
df -h | grep "home"
echo "--- SCANNING FOR OPEN PORTS ---"
nmap -F 127.0.0.1 | grep "open" || echo "No open ports found."
echo "--- CHECK COMPLETE ---"

