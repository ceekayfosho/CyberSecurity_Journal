#!/usr/bin/env python
import socket

IP = "0.0.0.0"
PORT = 4444

# Setup the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen(5)

print(f"[*] Persistent Listener active on {IP}:{PORT}...")

try:
    while True:
        # Wait for a connection
        client, addr = server.accept()
        print(f"[*] New connection from: {addr[0]}")

        try:
            # 1. Send the Banner
            banner = "--- SECURE MONITORING SYSTEM v1.0 ---\n"
            client.send(banner.encode('utf-8'))

            # 2. Log the Intruder to your file
            with open("network_logs.txt", "a") as log:
                log.write(f"Intruder detected from: {addr[0]}\n")

            # 3. Try to receive data (like Nmap probes)
            data = client.recv(1024)
            if data:
                # Use errors='replace' to prevent crashing on weird Nmap characters
                message = data.decode('utf-8', errors='replace').strip()
                print(f"[!] MESSAGE RECEIVED: {message}")

        except Exception as e:
            print(f"[!] Connection error: {e}")
        
        finally:
            # Always close the individual client connection
            client.close()

except KeyboardInterrupt:
    print("\n[!] Listener stopping...")

finally:
    # Shutdown the main server safely
    server.close()
    print("[*] Server socket closed.")
