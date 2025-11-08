import re

def is_phishing_link(link):
    suspicious_patterns = [
        r"https?://[^/\s]*@",
        r"[^\w\-\.]bit\.ly",
        r"tinyurl.*",
        r"http://[a-zA-Z0-9\-]+\.[a-z]{2,}",
        r".*[a-zA-Z0-9]{10,}\.[a-zA-Z]{2,}$"
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, link):
            return True
    return False