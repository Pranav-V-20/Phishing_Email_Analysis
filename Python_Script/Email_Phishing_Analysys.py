import re
import email
import tldextract
from bs4 import BeautifulSoup
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr
import tkinter as tk
from tkinter import filedialog, scrolledtext

# Sample list of known phishing phrases and suspicious keywords
PHISHING_KEYWORDS = [
    "your account has been compromised",
    "verify your identity",
    "urgent action required",
    "click here to reset",
    "login immediately",
    "unauthorized login attempt"
]

TRUSTED_DOMAINS = ['microsoft.com', 'paypal.com', 'google.com', 'apple.com']

def extract_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                return part.get_payload(decode=True).decode(errors='ignore')
            elif part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode(errors='ignore')
    else:
        return msg.get_payload(decode=True).decode(errors='ignore')
    return ""

def extract_links(email_body):
    soup = BeautifulSoup(email_body, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def check_domain_legitimacy(domain):
    ext = tldextract.extract(domain)
    full_domain = f"{ext.domain}.{ext.suffix}"
    return full_domain in TRUSTED_DOMAINS

def analyze_headers(headers):
    issues = []
    spf = dkim = dmarc = False

    for key, val in headers.items():
        if "spf=pass" in val.lower():
            spf = True
        if "dkim=pass" in val.lower():
            dkim = True
        if "dmarc=pass" in val.lower():
            dmarc = True

    if not spf:
        issues.append("SPF validation failed or missing.")
    if not dkim:
        issues.append("DKIM validation failed or missing.")
    if not dmarc:
        issues.append("DMARC validation failed or missing.")

    return issues

def detect_phishing_gui(email_file_path, output_widget):
    try:
        with open(email_file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
    except Exception as e:
        output_widget.insert(tk.END, f"[!] Error reading file: {e}\n")
        return

    body = extract_email_body(msg)
    from_name, from_addr = parseaddr(msg['From'])

    output_widget.insert(tk.END, f"From: {from_addr}\n")

    # Analyze sender domain
    ext = tldextract.extract(from_addr)
    sender_domain = f"{ext.domain}.{ext.suffix}"
    if sender_domain not in TRUSTED_DOMAINS:
        output_widget.insert(tk.END, f"[!] Suspicious sender domain: {from_addr}\n")

    # Check for phishing phrases
    lower_body = body.lower()
    for phrase in PHISHING_KEYWORDS:
        if phrase in lower_body:
            output_widget.insert(tk.END, f"[!] Found phishing phrase: '{phrase}'\n")

    # Analyze links
    links = extract_links(body)
    for link in links:
        ext = tldextract.extract(link)
        domain = f"{ext.domain}.{ext.suffix}"
        if domain not in TRUSTED_DOMAINS:
            output_widget.insert(tk.END, f"[!] Suspicious link domain found: {link}\n")

    # Analyze headers
    header_issues = analyze_headers(msg)
    for issue in header_issues:
        output_widget.insert(tk.END, f"[!] Header issue: {issue}\n")

    output_widget.insert(tk.END, "\n[+] Analysis complete.\n\n")

def browse_file(output_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Email files", "*.eml")])
    if file_path:
        output_widget.delete(1.0, tk.END)
        detect_phishing_gui(file_path, output_widget)

# GUI setup
def create_gui():
    root = tk.Tk()
    root.title("Phishing Email Analyzer")
    root.geometry("700x500")

    label = tk.Label(root, text="Select a .eml file to analyze:")
    label.pack(pady=10)

    browse_button = tk.Button(root, text="Browse .eml File", command=lambda: browse_file(output_text))
    browse_button.pack(pady=5)

    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
    output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
