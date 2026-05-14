#!/usr/bin/env python
import socket

IP = "0.0.0.0"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5) # Allow a small queue of callers

print(f"[*] Persistent Listener active on {IP}:{PORT}...")

try:
    while True:
        client, addr = server.accept()
        # Send a 'Banner' to the caller
        banner = "--- SECURE MONITORING SYSTEM v1.0 ---\n"
        client.send(banner.encode('utf-8'))

        print(f"[*] New connection from: {addr[0]}")
        
        data = client.recv(1024)
        if data:
            message = data.decode('utf-8').strip()
            print(f"[!] MESSAGE RECEIVED: {message}")
            
        client.close()
        print("[*] Waiting for next connection...")
except KeyboardInterrupt:
    print("\n[!] Listener stopping...")
finally:
    server.close()

