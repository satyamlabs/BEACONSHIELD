import os
import json
from logger import log_result
from phishing_link_detector import is_phishing_link

def load_config():
    with open("config.json") as f:
        return json.load(f)

def scan_file_for_keywords(filepath):
    config = load_config()
    try:
        with open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()

        matches_found = []
        for keyword in config['malicious_keywords']:
            if keyword.lower() in content.lower():
                matches_found.append(keyword)

        phishing_links = []
        for domain in config['phishing_domains']:
            phishing_links.extend([line.strip() for line in content.splitlines() if domain in line])

        result_data = {
            "file": filepath,
            "malicious_keywords_detected": matches_found,
            "phishing_links_found": [link for link in phishing_links if is_phishing_link(link)]
        }

        log_result(result_data)
        return result_data

    except Exception as e:
        print(f"[ERROR] Could not scan file {filepath}: {str(e)}")
        return None


def scan_directory(path):
    scan_summary = {"total_files_scanned": 0, "issues_found": []}
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            result = scan_file_for_keywords(filepath)
            scan_summary["total_files_scanned"] += 1
            if result:
                scan_summary["issues_found"].append(result)
    return scan_summary