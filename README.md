# 🛡️ Network Outbound Monitor

A simple Python script to detect outgoing network connections to public IPs. Useful for quick audits, malware detection, or blue team learning purposes.

## 📦 Features

- Scans all current outbound TCP connections
- Identifies connections to public IPs
- Retrieves geolocation and ISP info via [ipinfo.io](https://ipinfo.io)
- Compatible with Windows / Linux

## 🧪 Requirements

```bash
pip install psutil requests
```

🚀 Usage

```bash
python network_monitor.py
```

💡 Example Output

```yaml
[!] Connexion vers IP publique : 104.26.3.2 | PID: 2341
    ➜ Fournisseur: Cloudflare, Ville: Paris, Pays: FR
------------------------------------------------------------
```
