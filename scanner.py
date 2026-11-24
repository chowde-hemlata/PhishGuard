
import re
import ipaddress
from urllib.parse import urlparse


def analyze_url(url):

    results = []
    risk_score = 0

    parsed = urlparse(url)
    domain = parsed.hostname or ""

    # Check 1: HTTPS
    if parsed.scheme != "https":
        risk_score += 10
        results.append("Warning: URL does not use HTTPS")
    else:
        results.append("HTTPS connection detected")

    # Check 2: IP address in URL
    try:
        ipaddress.ip_address(domain)
        risk_score += 25
        results.append("Warning: Website uses an IP address")
    except ValueError:
        results.append("Domain name detected")

    # Check 3: Suspicious keywords
    keywords = [
        "login", "verify", "account",
        "banking", "password", "secure",
        "update", "free", "wallet"
    ]

    found_keywords = [
        word for word in keywords
        if word in url.lower()
    ]

    if found_keywords:
        risk_score += min(len(found_keywords) * 5, 20)
        results.append(
            "Suspicious keywords: " + ", ".join(found_keywords)
        )

    # Check 4: Excessive subdomains
    if len(domain.split(".")) > 3:
        risk_score += 15
        results.append("Warning: Excessive subdomains detected")

    # Check 5: URL length
    if len(url) > 75:
        risk_score += 10
        results.append("Warning: Unusually long URL")

    risk_score = min(risk_score, 100)

    if risk_score >= 50:
        verdict = "High Risk"
    elif risk_score >= 25:
        verdict = "Suspicious"
    else:
        verdict = "Low Risk"

    return {
        "risk_score": risk_score,
        "verdict": verdict,
        "details": results
    }
