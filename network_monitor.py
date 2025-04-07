# network_monitor.py
import psutil
import socket
import requests

def is_public_ip(ip):
    private_ranges = [
        ("10.0.0.0", "10.255.255.255"),
        ("172.16.0.0", "172.31.255.255"),
        ("192.168.0.0", "192.168.255.255"),
        ("127.0.0.0", "127.255.255.255")
    ]
    ip_addr = int.from_bytes(socket.inet_aton(ip), 'big')
    for start, end in private_ranges:
        if int.from_bytes(socket.inet_aton(start), 'big') <= ip_addr <= int.from_bytes(socket.inet_aton(end), 'big'):
            return False
    return True

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        return response.json()
    except:
        return {"error": "lookup failed"}

def scan_connections():
    connections = psutil.net_connections()
    seen_ips = set()

    for conn in connections:
        if conn.raddr and conn.status == 'ESTABLISHED':
            ip = conn.raddr.ip
            pid = conn.pid

            if ip not in seen_ips and is_public_ip(ip):
                seen_ips.add(ip)
                info = get_ip_info(ip)
                print(f"[!] Connexion vers IP publique : {ip} | PID: {pid}")
                print(f"    ➜ Fournisseur: {info.get('org', 'N/A')}, Ville: {info.get('city', 'N/A')}, Pays: {info.get('country', 'N/A')}")
                print("-" * 60)

if __name__ == "__main__":
    print("[*] Scan des connexions réseau sortantes en cours...\n")
    scan_connections()
