import re
import tkinter as tk
from tkinter import messagebox

# List of suspicious words with custom risk weights
phishing_words = {
    "urgent": 10,
    "verify": 5,
    "password": 5,
    "bank": 2,
    "click here": 10,
    "login": 3,
    "suspended": 8,
    "security alert": 8,
    "unusual activity": 8,
    "transactions": 3,
    "reset your password": 12,
    "verify your account": 12,
    "limited time": 8,
    "immediately": 8,
    "suspicious": 5,
    "temporary suspension": 12
}

def analyze_email():
    email_text = text_box.get("1.0", tk.END).lower()

    score = 0
    detected_words = []

    for word, weight in phishing_words.items():
        if word in email_text:
            score += weight
            detected_words.append(f"{word} (+{weight})")

    urls = re.findall(r'https?://\S+', email_text)
    if urls:
        score += 20
        detected_words.append("Contains Links (+20)")

    if score > 100:
        score = 100


    # Risk evaluation
    if score >= 50:
        result = "HIGH RISK: Possible Phishing Email"
    elif score >= 20:
        result = "WARNING: Suspicious Email"
    else:
        result = "CLEAR: Safe Email"

    output = f"{result}\n\nRisk Score: {score}%\n\nDetected Words:\n"

    if detected_words:
        for word in detected_words:
            output += f"- {word}\n"
    else:
        output += "None"

    messagebox.showinfo("Analysis Result", output)


# GUI Setup
window = tk.Tk()
window.title("PhishGuardCore-Local Analyzer")
window.geometry("600x400")

title = tk.Label(window, text="Email Content Threat Analyzer", font=("Arial", 18, "bold"))
title.pack(pady=20)

label = tk.Label(window, text="Paste Email Content Below")
label.pack()

text_box = tk.Text(window, height=12, width=70)
text_box.pack(pady=10)

analyze_button = tk.Button(window, text="Run Analysis", command=analyze_email, font=("Arial", 14, "bold"))
analyze_button.pack(pady=10)

window.mainloop()




