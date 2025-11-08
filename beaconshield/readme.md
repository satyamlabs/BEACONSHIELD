# 🛡️ BeaconShield

**BeaconShield** is an intelligent, lightweight cybersecurity tool built in Python. It scans files and directories to detect potential threats like phishing links, malicious keywords, and suspicious content changes. It also provides real-time monitoring capabilities with secure result logging for post-analysis.

Whether protecting personal documents or corporate data, BeaconShield helps you stay ahead of digital dangers.

---

## 🔍 Key Features

✅ **Malicious Keyword Detection**: Identify common exploit patterns and dangerous keywords  
✅ **Phishing Link Recognition**: Flag risky URLs based on domain reputation & structure  
✅ **Scan Directories On-Demand**: Perform one-time deep scans  
✅ **Real-Time Monitoring Mode**: Automatically watch any folder for updates  
✅ **Detailed Logging Engine**: Structured JSON-format logs saved for review  

---

## 📦 Requirements

Python ≥ 3.7 installed  
Additional libraries:

```bash
pip install watchdog
```

No admin/root privileges required unless accessing protected directories.

---

## 🧪 Quick Start Guide

### Step 1: Clone/Download Repo

Either download `.zip` from GitHub or clone via terminal:

```bash
git clone https://github.com/yourusername/beaconshield.git
cd beaconshield
```

### Step 2: Install Dependencies

Make sure Python 3.x is installed, then install required packages:

```bash
pip install watchdog
```

That's it! No additional installs needed.

---

## 🚀 Getting Started With Commands

All commands are run using the `main.py` file located in the project root.

### ➤ To Scan a Folder Once:
Scans entire selected directory recursively.

```bash
python main.py scan /path/to/directory
```

**Result**: Outputs a summary including issue reports and counts of scanned files.

Sample Output:
```json
{
  "total_files_scanned": 56,
  "issues_found": [
    {
      "file": "/home/user/documents/suspicious.txt",
      "malicious_keywords_detected": ["password"],
      "phishing_links_found": ["http://bit.ly/virusdownload"]
    }
  ]
}
```

Logs also get written to `scan_results.log`.

---

### ➤ To Monitor a Folder in Background (Start):

Begin real-time tracking of a specified path:

```bash
python main.py monitor start /path/to/watch
```

A `.beaconshield.pid` file will appear during active monitoring.

📌 *Note*: Only one instance supported at a time (by design).

---

### ➤ To Stop Background Monitoring:

End live tracking started earlier.

```bash
python main.py monitor stop
```

Deletes PID file upon successful shutdown.

📝 *Tip:* Stale PIDs auto-clean if their process was already terminated.

---

## 📄 Configuration

Edit the `config.json` file to define custom rulesets and threat indicators:

```json
{
    "malicious_keywords": [
        "password",
        "credit card",
        "__import__",
        "eval"
    ],
    "phishing_domains": [
        "bit.ly",
        "tinyurl.com"
    ]
}
```

Customize based on your environment's norms and policies.

---

## 📚 Output & Logs

All results are automatically appended in JSON-formatted entries inside `scan_results.log`. Sample log entry:

```json
{
  "timestamp": "2025-11-08T12:34:56.789Z",
  "data": {
    "file":"./example_file.txt",
    "malicious_keywords_detected": ["eval"],
    "phishing_links_found": ["https://tinyurl.com/badpage"]
  }
}
```

These entries make automated parsing or SIEM integrations straightforward.

---

## ✅ Benefits For Users

| Feature                 | Why It Matters |
|------------------------|----------------|
| Real-time Protection   | React instantly to new threats entering monitored paths |
| Easy Script Automation | Can be integrated into CRON jobs or CI pipelines |
| Portable Design        | Run anywhere Python exists (Windows/Linux/macOS) |
| Lightweight Footprint  | Minimal CPU/memory impact during continuous operation |
| Extensible Framework   | Modular code makes it easy to plug in new detectors |

---

## 📜 Future Enhancements (Roadmap Ideas)

- Integrating online virus scanners like VirusTotal
- Machine learning anomaly detection module
- Web dashboard visualizing logs
- Packaging as executable with PyInstaller
- Email/SMS alert support when threats detected

---

## 🤝 Contributing

Want to contribute?

1. Fork the repo
2. Make your improvements
3. Submit a Pull Request

Suggestions welcome!

---

## ⚖ License

This project is released under the MIT License. See [`LICENSE`](./LICENSE) for details.

--- 