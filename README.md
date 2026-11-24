# PhishGuard – Intelligent Phishing URL Detection System

## 1. Project Overview

PhishGuard is a web-based phishing URL detection system designed to analyze URLs and identify potentially suspicious characteristics.

Phishing attacks use deceptive websites and URLs to trick users into revealing sensitive information such as passwords, banking details and personal data.

PhishGuard evaluates multiple URL characteristics, calculates a risk score and provides an understandable verdict to help users recognize potentially dangerous links.

## 2. Objectives

- Identify potentially suspicious URLs.
- Analyze URL characteristics using predefined security rules.
- Calculate a risk score between 0 and 100.
- Classify URLs according to their assessed risk.
- Display the reasons contributing to the risk assessment.

## 3. Features

- **HTTPS Analysis:** Checks whether the URL uses HTTPS.
- **IP Address Detection:** Identifies URLs that use an IP address instead of a domain name.
- **Suspicious Keyword Detection:** Checks for keywords such as login, verify, password, banking and wallet.
- **Subdomain Analysis:** Detects URLs containing excessive subdomains.
- **URL Length Analysis:** Flags unusually long URLs.
- **Risk Scoring:** Assigns a score based on detected indicators.
- **Risk Classification:** Categorizes results as Low Risk, Suspicious or High Risk.
- **Explainable Results:** Displays the reasons behind the assessment.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming and URL analysis |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | User interface styling |
| Git | Version control |
| GitHub | Source code hosting |

## 5. Risk Assessment Methodology

PhishGuard uses a rule-based heuristic approach.

The scanner evaluates five URL characteristics:

| Indicator | Risk Score |
|---|---:|
| URL does not use HTTPS | +10 |
| IP address used as hostname | +25 |
| Suspicious keywords | +5 per keyword, maximum +20 |
| More than three domain components | +15 |
| URL longer than 75 characters | +10 |

The total score is capped at 100.

### Risk Classification

| Risk Score | Classification |
|---|---|
| 0–24 | Low Risk |
| 25–49 | Suspicious |
| 50–100 | High Risk |

## 6. Project Structure

```text
PhishGuard/
│
├── app.py
├── scanner.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── .gitignore
```

## 7. Installation and Execution

### Prerequisites
- Python 3
- pip
- Git

### Steps

1. Clone the repository:

```bash
git clone https://github.com/chowde-hemlata/PhishGuard.git
```

2. Navigate to the project directory:

```bash
cd PhishGuard
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

6. Run the application:

```bash
python app.py
```

7. Open the application in your browser using the local address displayed in the terminal.

## 8. Limitations

- The current detection system uses predefined heuristic rules rather than a trained machine learning model.
- A low-risk result does not guarantee that a website is legitimate or safe.
- A suspicious characteristic does not necessarily mean that a URL is malicious.
- The system does not currently establish a definitive verdict using a live phishing threat-intelligence database.

## 9. Future Enhancements

- Integration of machine learning-based phishing detection.
- Domain age and registration analysis.
- DNS and SSL certificate analysis.
- Integration with external threat-intelligence databases.
- Scan history and reporting dashboard.
- Improved detection accuracy through larger datasets and testing.

## 10. Conclusion

PhishGuard demonstrates a practical approach to identifying potentially suspicious URLs through rule-based analysis and risk scoring.

The project aims to make URL security analysis more understandable by presenting both a risk classification and the indicators contributing to it.

## 11. Project Links

**GitHub Repository:**  
https://github.com/chowde-hemlata/PhishGuard

---

*Disclaimer: PhishGuard is an educational cybersecurity project. Its results are indicative assessments and should not be treated as a guarantee of website safety.*