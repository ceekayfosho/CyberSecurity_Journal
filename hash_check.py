#!/usr/bin/env python
import hashlib
from datetime import datetime

def get_hash(filename):
    hasher = hashlib.sha256()
    try:
        with open(filename, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

log_file = 'network_logs.txt'
fingerprint = get_hash(log_file)

if fingerprint:
    # This creates a permanent record for your 'Audit'
    with open('hash_manifest.txt', 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} | {log_file} | {fingerprint}\n")
    print(f"Verified: {fingerprint}")
    print("Hash added to hash_manifest.txt")

