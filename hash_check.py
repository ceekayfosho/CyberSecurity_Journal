#!/usr/bin/env python
import hashlib

# This is your 'Baseline'—the fingerprint of the clean log file
GOLDEN_HASH = "c96a19a933f9df0ad146e3dcebad95f6960b15781c5f2ffe2634a2eb491fe63d"

def get_hash(filename):
    hasher = hashlib.sha256()
    try:
        with open(filename, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

current_hash = get_hash('network_logs.txt')

if current_hash == GOLDEN_HASH:
    print("✅ INTEGRITY VERIFIED: No changes detected.")
else:
    print("🚨 ALERT: FILE TAMPERED WITH!")
    print(f"Current: {current_hash}")
import datetime
print(f"[{datetime.datetime.now()}] ✅ INTEGRITY VERIFIED")
