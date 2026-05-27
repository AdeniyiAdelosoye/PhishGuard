# PhishGuard
PhishGuard is a simple rule based phishing email detection system built with Python and Tkinter.

The project analyzes email content using keyword matching and basic threat scoring techniques to identify potentially suspicious or phishing related emails.

This project was created as a beginner cybersecurity and software engineering experiment to explore how phishing detection systems can work at a basic level. It was not designed to be a production level security tool or an advanced AI system. 

The purpose of the project is to demonstrate the combination of:
- Cybersecurity concepts
- Python programming
- GUI development
- Threat analysis logic
- Software engineering fundamentals

## 🚀 Features
* **Interactive GUI:** Easy-to-use desktop interface built with Tkinter.
* **Weighted Scoring System:** Analyzes email content for common phishing keywords and patterns.
* **Link Detection:** Identifies risky URLs or misleading hyperlinks within the text.

## How It Works

The application scans email text for suspicious indicators such as:
- urgent language
- password requests
- account verification prompts
- suspicious links
- banking related threats

Each detected indicator increases the overall phishing score.

Based on the final score, the email is classified as:
- Safe
- Suspicious
- High Risk Phishing

## Example Detection

⚠️ HIGH RISK: Possible Phishing Email

Risk Score: 75%

Detected Indicators:
- urgent
- verify
- password
- suspicious
- online banking
- https://secure-novatrust-alert.com/verify

## 🛠️ Built With
* **Python** (Core logic and phishing detection system)
* **Tkinter** (Graphical User Interface)
* **Regular Expressions - `re`** (URL and pattern detection)
* **Git** (Version control)
* **GitHub** (Project hosting and deployment)

## 📦 How to Run the Project

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open a terminal or command prompt in the project directory.
4. Run the following command:

```bash
python phishing_detector.py
```

5. Paste an email into the application window.
6. Click "Run Analysis" to scan for phishing indicators.


## Disclaimer

This project is intended strictly for educational and demonstration purposes.

The emails, links, institutions, and examples used in this project are fictional and were created only for testing the detection system.

PhishGuard is not intended to impersonate real organizations or be used for malicious activity.
