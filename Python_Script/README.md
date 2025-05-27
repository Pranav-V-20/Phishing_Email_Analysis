# 🛡️ Phishing Email Analyzer (with GUI)

This Python tool allows you to **analyze `.eml` email files** for signs of phishing using:

- Heuristic keyword matching
- Link and domain analysis
- Email header checks (SPF, DKIM, DMARC)
- A clean, interactive GUI (built with Tkinter)

It’s especially useful for cybersecurity researchers, educators, and SOC analysts.

---

## 📸 GUI Preview

![Preview](https://github.com/user-attachments/assets/a5d4078b-4e21-4dd6-a06b-416997389f57)

---

## 🚀 Features

✅ Analyze `.eml` files for:
- Phishing keywords and urgency tactics  
- Suspicious sender domains  
- Malicious-looking hyperlinks  
- Missing or failing SPF, DKIM, and DMARC validations

✅ Browse `.eml` files via a **Tkinter-based GUI**  
✅ Outputs readable, scrollable results  
✅ Easy-to-extend architecture

---

## 📦 Requirements

Make sure you have the following packages installed:

```bash
pip install tldextract beautifulsoup4 dnspython
