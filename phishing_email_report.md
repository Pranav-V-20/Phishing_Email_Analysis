## **Phishing Email Analysis Report**

**Email Subject**: Microsoft account password change

**Sender**: `Support <support@msupdate.net>`

**Recipient**: [ethan@hooksecurity.co](mailto:ethan@hooksecurity.co)

**Analyzed On**: May 27, 2025

**Analyzed By**: Pranav V

---

### **1. Sender Email Address Analysis**

* **Displayed Sender**: “Support”
* **Email Address**: `support@msupdate.net`
* **Issue**: The domain `msupdate.net` is **not associated with Microsoft**. A legitimate Microsoft email would come from `@microsoft.com` or a related subdomain (e.g., `account-security-noreply@accountprotection.microsoft.com`).
* **Indicator**: ***Spoofed or misleading sender domain***

---

### **2. Header Analysis**

**(Header not provided in the image, but we can infer possible issues. Ideally, use a tool like MxToolbox to confirm.)**

Potential issues to look for:

* SPF or DKIM failures (indicating spoofed email source).
* Mismatched Return-Path or Reply-To addresses.
* Relayed through non-Microsoft mail servers.

---

### **3. Suspicious Links or Attachments**

* **Links Present**:

  1. Reset your password
  2. Review your security info
  3. Learn how to make your account more secure
  4. Opt out
* **Issue**: The real URL is not visible in the image. **Hovering over links in a real email** would reveal if they lead to suspicious or non-Microsoft domains.
* **Recommendation**: Always **hover over links** to verify the domain matches Microsoft (e.g., `https://account.microsoft.com/`).

---

### **4. Language and Tone**

* **Tone**: Calm but implies urgency and security risk if the action wasn't taken by the user.
* **Phrase**: "If this wasn't you, your account has been compromised."
* **Indicator**: This is common phishing tactic — scare the user into quickly clicking a link.

---

### **5. Spelling and Grammar Check**

* No noticeable grammar or spelling errors in the visible content.
* This is consistent with more **sophisticated phishing** attempts that avoid typos to appear legitimate.

---

### **6. Mismatched URLs**

* Not viewable in the image; in a live email, you should:

  * Hover over each hyperlink
  * Verify the actual link matches the anchor text
* If any link points to a domain like `security-microsoftlogin.com` or shortened URLs, it's suspicious.

---

### **7. Visual Indicators**

* The email is styled to **mimic a legitimate Microsoft notification**, including formatting and terminology.
* However, the **sender domain** is a critical red flag.
* **No Microsoft logo** is present — often phishing emails omit real branding assets to avoid copyright detection by filters.

---

### **8. Summary of Phishing Traits**

| Indicator                  | Details                                              |
| -------------------------- | ---------------------------------------------------- |
| **Spoofed Sender Address** | `@msupdate.net` is not a Microsoft domain.           |
| **Threatening Language**   | “Your account has been compromised.”                 |
| **Suspicious Links**       | Links are likely hidden and may not go to Microsoft. |
| **Lack of Branding**       | No logo or verified sender info present.             |
| **Call to Action**         | Pushes the user to click links under pressure.       |

---

## **Conclusion**

This email is **likely a phishing attempt** designed to impersonate Microsoft and trick the user into clicking malicious links under the pretense of a security notification.

---

## **Recommendations**

1. Do **not click** any links or download attachments.
2. Report the email to your IT/Security team or Microsoft.
3. Mark the email as spam or phishing in your email client.
4. Educate users on identifying spoofed domains and phishing language.
