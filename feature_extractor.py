from urllib.parse import urlparse
import re

def extract_features(url):

    features = []

    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('/'))

    features.append(1 if url.startswith("https") else 0)

    features.append(1 if '@' in url else 0)

    ip_pattern = r'(\d+\.){3}\d+'
    features.append(1 if re.search(ip_pattern, url) else 0)

    suspicious_words = [
        'login',
        'verify',
        'secure',
        'account',
        'update',
        'bank'
    ]

    count = 0

    for word in suspicious_words:
        if word in url.lower():
            count += 1

    features.append(count)

    return features