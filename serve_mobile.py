import http.server
import socketserver
import socket
import subprocess
import threading
import sys
import os

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"[+] Local HTTP Server running on port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    local_ip = get_local_ip()
    print("=" * 65, flush=True)
    print("        SENTINELAI MOBILE LIVE DEMO LAUNCHER", flush=True)
    print("=" * 65, flush=True)
    print(f"\n[1] LOCAL NETWORK URL (If on Mobile Hotspot):", flush=True)
    print(f"    http://{local_ip}:{PORT}/mobile_sentinel.html", flush=True)
    print(f"\n[2] LOCALHOST (On this laptop):", flush=True)
    print(f"    http://localhost:{PORT}/mobile_sentinel.html", flush=True)
    print("\n" + "-" * 65, flush=True)
    print("[3] ZERO-WIFI / 4G / 5G ACCESS (Using Localtunnel):", flush=True)
    print("    Starting public tunnel so any phone can open it anywhere...", flush=True)
    print("=" * 65, flush=True)

    # Start local server in background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Try starting localtunnel
    try:
        tunnel = subprocess.Popen(
            "npx --yes localtunnel --port 8080",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        print("\n[+] Generating Global HTTPS link for mobile phone...", flush=True)
        for line in tunnel.stdout:
            if "your url is:" in line.lower():
                clean_url = line.strip().split()[-1]
                print(f"\n==================================================", flush=True)
                print(f"  >>> MOBILE PUBLIC LINK: {clean_url} <<<", flush=True)
                print(f"  Direct App: {clean_url}/mobile_sentinel.html", flush=True)
                print(f"==================================================", flush=True)
                print("\nPHONE PE KAISE KHOLNA HAI:", flush=True)
                print(f"1. Phone Chrome me link kholein: {clean_url}/mobile_sentinel.html", flush=True)
                break
    except Exception as e:
        print(f"[-] Tunnel error: {e}", flush=True)

    print("\n[Server is active. Press Ctrl+C to stop]", flush=True)
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping server...")
