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

# Function to analyze email

def analyze_email():
    # 1. Get the text from the text box
    email_text = text_box.get("1.0", tk.END).lower()

    # 2. Initialize your score and tracking list (CRITICAL STEP)
    score = 0
    detected_words = []

    # 3. Check for dictionary keywords (Replaces BOTH old loops)
    for word, weight in phishing_words.items():
        if word in email_text:
            score += weight
            detected_words.append(f"{word} (+{weight})")

    # 4. Detect suspicious links (Your existing link logic)
    urls = re.findall(r'https?://[^\s]+', email_text)
    if urls:
        score += 20
        detected_words.append("Contains Links (+20)")

    # Limit score to 100
    if score > 100:
        score = 100


    # Risk evaluation
    if score >= 50:
        result = "HIGH RISK: Possible Phishing Email"
    elif score >= 20:
        result = "Suspicious Email"
    else:
        result = " Safe Email"

    # Show results
    output = f"{result}\n\nRisk Score: {score}%\n\nDetected Words:\n"

    if detected_words:
        for word in detected_words:
            output += f"- {word}\n"
    else:
        output += "None"

    messagebox.showinfo("Analysis Result", output)


# GUI Window
window = tk.Tk()
window.title("Phishing Emial Detector")
window.geometry("600x400")

# TITLE
title = tk.Label(window, text="AI Phishing Email Detector", font=("Arial", 18))
title.pack(pady=20)

#Instructions
label = tk.Label(window, text="Paste Email Content Below")
label.pack()


#  Text box
text_box = tk.Text(window, height=12, width=70)
text_box.pack(pady=10)

# Analyze button
analyze_button = tk.Button(window, text="Analyze Email", command=analyze_email)
analyze_button.pack(pady=10)

# Run app
window.mainloop()




