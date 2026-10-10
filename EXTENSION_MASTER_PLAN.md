# SentinelAI — Browser Extension Master Plan & Technical Documentation

> **Project Name:** SentinelAI On-Device Threat Shield  
> **Platform:** Google Chrome, Microsoft Edge, Brave Browser (Manifest V3)  
> **Location:** `d:\spam detection\sentinelai-extension`  
> **Privacy Invariant:** 100% On-Device Execution · Zero External Cloud Requests · Airplane Mode Ready  

---

## 1. Product Vision & The Core Idea

In enterprise and corporate office work, over **90% of phishing attacks and social engineering scams** happen inside desktop web browsers via:
- Webmail (Gmail, Outlook 365)
- Internal communication tools (Slack, Teams, Telegram Web, WhatsApp Web)
- Lookalike banking portals and fake corporate SSO login pages

### Why the Browser Extension is the Ultimate Hackathon Solution:
1. **Zero Dangerous Mobile Permissions:** No SMS reader or background listener restrictions.
2. **True On-Device Privacy:** The user's emails and links never touch any third-party server.
3. **Cross-Platform Compatibility:** Runs universally on Windows laptops, MacBooks, Linux workstations, and Chromebooks.
4. **Immediate Judge Demo:** Mentors see real-time link highlighting, right-click inspections, and instant popup scans right in their browser.

---

## 2. System Architecture & Component Breakdown

```
┌────────────────────────────────────────────────────────────────────────┐
│                        CHROME / EDGE BROWSER                           │
│                                                                        │
│   ┌────────────────────────┐           ┌────────────────────────────┐  │
│   │   ACTIVE WEB PAGES     │           │    POPUP INTERFACE         │  │
│   │ (Gmail, Outlook, Web)  │           │   (popup.html / .js)       │  │
│   └───────────┬────────────┘           └──────────────┬─────────────┘  │
│               │ (Passive Link Hover)                  │ (Manual Scan)  │
│               ▼                                       ▼                │
│   ┌────────────────────────┐           ┌────────────────────────────┐  │
│   │      content.js        │           │     DUAL ON-DEVICE         │  │
│   │  • Red highlight       │           │        ENGINES             │  │
│   │  • Intercepts clicks   │◄─────────►│  • urlAnalyzer.js          │  │
│   │  • Injects banner      │           │  • messageAnalyzer.js      │  │
│   └───────────┬────────────┘           └──────────────┬─────────────┘  │
│               │                                       │                │
│               ▼                                       ▼                │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │                  background.js (Service Worker)                │   │
│   │   • Right-Click Context Menu ("Inspect with SentinelAI")       │   │
│   │   • Desktop System Notifications                               │   │
│   │   • Dynamic Badge Icon (CRIT / WARN / SAFE)                    │   │
│   └────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Directory & File Structure

```
d:\spam detection\sentinelai-extension\
├── manifest.json         # Manifest V3 configuration & browser permissions
├── background.js         # Service worker: handles right-click & notifications
├── content.js            # Injected script: live link hovering & click protection
├── urlAnalyzer.js        # On-device lexical URL engine (Shannon entropy, Levenshtein)
├── messageAnalyzer.js    # On-device NLP psychological lure extractor (6 vectors)
├── popup.html            # Dark cybersecurity extension UI
├── popup.css             # CrowdStrike / Linear inspired styling
├── popup.js              # Popup controller & manual instant scanner
└── icons/
    ├── icon16.png        # Toolbar icon (16x16)
    ├── icon48.png        # Extension management icon (48x48)
    └── icon128.png       # Chrome Web Store & Notification icon (128x128)
```

---

## 4. The 4 Killer Features Built Into the Extension

### Feature 1: Passive On-Page Link Guard (`content.js`)
* As the user reads emails or browses websites, any link they hover over is analyzed in **< 2 milliseconds**.
* If a domain has high Shannon entropy or typosquats a major brand (e.g., `sbi-secure.xyz`), the extension adds a **dashed red outline** and displays a warning tooltip.
* If the user accidentally clicks a high-risk link, SentinelAI **intercepts the click** and displays an on-screen confirmation modal.

### Feature 2: Right-Click "Zero-Cloud" Inspection (`background.js`)
* Highlight any text on any website or email -> **Right Click** -> Select:
  - `🛡️ SentinelAI: Scan Text for Scams (On-Device)`
  - `🛡️ SentinelAI: Inspect Link for Phishing (On-Device)`
* A native browser notification appears immediately with the Threat Score and detected psychological lures.

### Feature 3: Live Active Tab Safety Badge
* The extension icon dynamically displays a badge on your toolbar:
  - 🟢 `SAFE` for verified legitimate domains
  - 🟡 `WARN` for unverified or suspicious parameters
  - 🔴 `CRIT` for confirmed typosquatting or phishing pretexts

### Feature 4: Popup Manual Threat Lab (`popup.html`)
* Shows active page telemetry (Shannon entropy, Risk Index).
* Allows employees to paste any SMS or link into the quick scanner for instant local analysis with an **Automated Incident Containment Playbook**.

---

## 5. How to Load & Test in Chrome / Edge (In 60 Seconds)

1. Open **Google Chrome** (or **Microsoft Edge** / **Brave**).
2. In the address bar, type:
   - For Chrome: `chrome://extensions`
   - For Edge: `edge://extensions`
3. In the top right corner, **turn ON "Developer mode"**.
4. Click the button: **"Load unpacked"**.
5. Select the folder:
   👉 `D:\spam detection\sentinelai-extension`
6. Click **Select Folder**.  
   *Result:* The **SentinelAI Threat Shield** icon will appear on your browser toolbar!

---

## 6. Hackathon Live Demo Script (For Mentors)

```text
[Step 1 - The Setup]
"Mentors, for enterprise office environments, we built SentinelAI as a 
zero-cloud Manifest V3 browser extension to protect corporate webmail and browsing."

[Step 2 - The Offline Proof]
Turn off Wi-Fi on your laptop (Airplane Mode).
"Notice that Wi-Fi is completely disabled. There are zero cloud network requests."

[Step 3 - The Extension Popup]
Click the SentinelAI shield icon in Chrome.
Paste: "URGENT: SBI account suspended. Update KYC in 2 hours: http://sbi-secure-update.xyz"
Click "Scan On-Device".
"In under 5 milliseconds, it calculates a 92/100 Threat Index, identifies the 
2-hour urgency window and SBI impersonation, and outputs an incident recovery playbook."

[Step 4 - Right-Click Context Menu]
Highlight any suspicious text on a page -> Right click -> "Scan Text for Scams".
Show the instant native browser notification!
```
