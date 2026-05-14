#!/usr/bin/env python
import os
import subprocess
import time

def run_security_scan():
    print("[*] Watchman: Starting Integrity Scan...")
    
    # Run your hash check and capture the output
    result = subprocess.run(['python', 'hash_check.py'], capture_output=True, text=True)
    
    # Check if the output contains the 'ALERT' keyword
    if "ALERT" in result.stdout:
        print("🚨 ALERT DETECTED! Deploying Network Listener immediately...")
        # Start the listener
        os.system('python net_listener.py')
    else:
        print("✅ System Secure. No unauthorized changes.")

if __name__ == "__main__":
    while True:
        run_security_scan()
        print("[*] Next scan in 30 seconds...")
        time.sleep(30) # Wait 30 seconds before checking again

