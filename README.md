# SentinelAI — On-Device Threat, Phishing & Scam Intelligence System

> **Problem Statement PS-05:** *On-device threat, phishing and scam detection.*  
> **Privacy Invariant:** 100% On-Device Execution · Zero External Cloud Transmission · Complete Forensic Explainability.

---

## 1. Project Overview

**SentinelAI** is an enterprise-grade, privacy-first cybersecurity assistant that detects phishing URLs, smishing scams, credential harvesting portals, and psychological coercion lures directly on client hardware.

Traditional threat detection tools compromise user privacy by uploading private SMS messages, emails, and browsing history to third-party cloud servers. **SentinelAI eliminates this privacy risk entirely** by running dual on-device detection engines (Python FastAPI + Native Client JavaScript) that extract lexical heuristics, calculate psychological lure metrics, build NetworkX causal attack graphs, and generate forensic SHA-256 evidence provenance without sending a single byte of data off the user's device.

---

## 2. Software Prerequisites & Technology Stack

### Runtime & System Requirements
- **Operating System:** Windows 10/11, macOS, or Linux
- **Python Runtime:** Python `3.10` or higher (Tested & verified on Python `3.11`, `3.12`, `3.13`, `3.14`)
- **Web Browser:** Any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, Safari)
- **Node.js (Optional):** Node.js `v18+` (Only needed if running optional headless browser simulation test scripts)

### Technology Stack & Libraries

| Layer | Technologies & Libraries | Purpose / Role |
| :--- | :--- | :--- |
| **Browser Extension** | Chrome/Edge Manifest V3, WebNavigation, DeclarativeNetRequest, Shadow DOM | Enterprise browser guardian with zero-cloud DOM inspection & webmail security. |
| **On-Device ML Engine** | Scikit-Learn (TF-IDF + Logistic Regression) $\to$ Pure JS Runtime | Lightweight on-device text & URL ML models (< 100 KB JSON, < 2ms latency). |
| **Backend REST API** | `FastAPI`, `Uvicorn`, `Pydantic v2`, `pydantic-settings` | High-performance asynchronous REST microservices and OpenAPI documentation. |
| **Detection Engines** | Python `re`, `urllib.parse`, `math` (Shannon Entropy), `Levenshtein` | On-device lexical feature extraction, typosquatting detection, NLP psychological lure parsing. |
| **Causal Intelligence** | `NetworkX` | Directed Acyclic Graph (DAG) construction, attack chain modeling, defensive breakpoint calculation. |
| **Forensic & Provenance** | `hashlib` (SHA-256) | Deterministic cryptographic evidence provenance linking rule firings to raw tokens. |
| **Automated Verification** | `pytest`, `pytest-asyncio`, `httpx`, Node.js Test Suite (180 labeled samples) | 38 automated backend test suites + 180 extension regression/evaluation test suite. |
| **Documentation & PDF** | `reportlab` | Automated publication-grade PDF dossier generation. |
| **Frontend UI/UX** | HTML5, Modern CSS3, JavaScript (ES6+), Inline Vector SVGs | Enterprise Dark Cybersecurity SaaS Dashboard (0 emojis, CrowdStrike / Linear style). |

---

## 3. Step-by-Step Running Guide

### Step 1: Open Terminal & Navigate to Project Directory
Open **PowerShell**, **Command Prompt**, or **Terminal**:

```powershell
cd "D:\spam detection"
```

---

### Step 2: (Optional but Recommended) Create & Activate a Python Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Windows (CMD)
.\venv\Scripts\activate.bat

# Activate on Linux / macOS
source venv/bin/activate
```

---

### Step 3: Install Required Dependencies

Navigate into the backend folder and install all required Python packages:

```powershell
cd "D:\spam detection\sentinelai\backend"
pip install -r requirements.txt
```

---

### Step 4: Start the SentinelAI Server

Run the FastAPI application via Uvicorn:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

You will see the startup banner in your terminal:
```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

---

### Step 5: Open the Web Application in Your Browser

Open your browser and visit:

👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

- **Interactive API Documentation (Swagger / OpenAPI):**  
  👉 **[http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)**
- **Alternative Redoc API Documentation:**  
  👉 **[http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)**

---

## 4. Running the Automated Pytest Suite (38 Tests)

To verify the backend detection engine, risk scoring mathematics, and privacy guarantees:

```powershell
cd "D:\spam detection\sentinelai\backend"
pytest tests/ -v
```

### Test Suite Coverage (100% Passed · 38/38 Tests)
- `test_detection.py` (7 tests): Shannon entropy calculations, brand typosquatting, punycode evasion, raw IP URLs.
- `test_scan_api.py` (4 tests): REST endpoints for `/api/scan/url`, `/api/scan/message`, and unified `/api/scan`.
- `test_attack_simulator.py` (15 tests): NetworkX graph building, state transitions, interactive counterfactual simulations.
- `test_causal.py` (1 test): Causal attack progression DAG construction.
- `test_counterfactual.py` (2 tests): Risk gradient calculation upon removing threat signals.
- `test_robustness.py` (2 tests): Resistance against evasion mutations and signal ablation stress tests.
- `test_privacy.py` (2 tests): Asserts that zero raw user content or credentials are logged or leaked.
- `test_objective.py` (1 test): Attacker intent classification (Credential theft, Financial extortion).
- `test_recovery.py` (2 tests): Automated incident remediation playbook generation.
- `test_health.py` (1 test): Operational health and model signature check.

---

## 5. Project Directory Structure

```text
d:/spam detection/
│
├── SentinelAI_Complete_Project_Dossier.pdf  # Comprehensive Hackathon PDF Report
├── README.md                                # Project Documentation (This File)
│
└── sentinelai/
    ├── index.html                           # Main Enterprise Dashboard (HTML5)
    ├── favicon.svg                          # Vector Cybersecurity Shield Brand Logo
    │
    ├── css/
    │   └── styles.css                       # Enterprise Dark SaaS Theme (No emojis, crisp 1px borders)
    │
    ├── js/                                  # Modular On-Device JavaScript Engines
    │   ├── app.js                           # Main Controller & Navigation Coordinator
    │   ├── urlAnalyzer.js                   # Client-Side URL Feature & Entropy Extractor
    │   ├── messageAnalyzer.js               # Client-Side NLP Lure & Smishing Detector
    │   ├── riskEngine.js                    # Calibrated 0-100 Mathematical Risk Scoring
    │   ├── intelligenceEngine.js            # Pretexting Models & Evidence Chains
    │   ├── intelligenceUI.js                # Advanced Scorecards & Causal Views
    │   ├── threatLabEngine.js               # Synthetic Mutation & Red-Team Generator
    │   ├── threatLabUI.js                   # Threat Lab & Behavioral Clustering UI
    │   ├── counterfactualEngine.js          # Counterfactual Decision Simulators
    │   ├── counterfactualUI.js              # Interactive Threat Parameter Dial UI
    │   ├── researchLabEngine.js             # Real Measured Stability & Provenance Logic
    │   ├── researchLabUI.js                 # Research Intelligence Lab Suite UI
    │   ├── securityFirewall.js              # Client Policy Rules & Violations
    │   ├── securityMemory.js                # Privacy-Preserving Pattern Memory
    │   ├── localVerification.js             # Telemetry & Zero-Cloud Invariant Audit
    │   ├── dnaComparison.js                 # Multi-Sample Scam DNA Genetic Clustering
    │   ├── adversarialTester.js             # Homoglyph & Zero-Width Evasion Sandbox
    │   ├── backendClient.js                 # Resilient REST Synchronization Layer
    │   ├── attackSimulatorClient.js         # Interactive Attack Simulation Client
    │   └── demoScenarios.js                 # Pre-Configured Benchmark Demo Scenarios
    │
    └── backend/                             # Production Python FastAPI Engine
        ├── pytest.ini                       # Pytest Configuration
        ├── requirements.txt                 # Backend Python Dependencies
        │
        ├── app/
        │   ├── main.py                      # FastAPI Application Root & Static Mounter
        │   ├── core/                        # Configuration & Zero-Leakage Security Logs
        │   ├── db/                          # Local Database Initialization
        │   ├── engines/                     # Core URLDetector, MessageDetector, RiskScorer
        │   ├── intelligence/                # NetworkX Causal Graph, Objective & Recovery
        │   ├── schemas/                     # Pydantic Request & Response Models
        │   ├── services/                    # Analysis & Simulation Orchestrators
        │   └── api/routes/                  # REST API Route Endpoints
        │
        └── tests/                           # 38 Automated Pytest Suites
```

---

## 6. REST API Endpoints Overview

| Endpoint | Method | Request Payload | Description |
| :--- | :--- | :--- | :--- |
| `/api/scan/url` | `POST` | `{"url": "http://example.com"}` | Scans URL for typosquatting, entropy, suspicious TLDs, IP hosts. |
| `/api/scan/message` | `POST` | `{"content": "Urgent..."}` | Parses SMS/email for 6 psychological lures, OTP requests, and links. |
| `/api/scan` | `POST` | `{"type": "url", "content": "..."}` | Unified auto-routing detection endpoint. |
| `/api/intelligence/causal-graph` | `POST` | `{"signals": [...]}` | Builds NetworkX causal DAG and identifies defensive breakpoints. |
| `/api/intelligence/counterfactual`| `POST` | `{"signals": [...], "modifications": {...}}` | Recalculates risk when threat parameters are modified. |
| `/api/health` | `GET` | *None* | Health status, signature version, local privacy guarantee. |

---

## 7. Hackathon Judge Demo Test Cheat-Sheet

Use these pre-tested test samples during live judge presentations:

### Test Scenario 1: Urgent Banking KYC Phishing (High Risk)
- **Input Text:**
  ```text
  URGENT: Dear Customer, your SBI bank account has been SUSPENDED due to incomplete KYC. Your account will be permanently blocked in 2 hours. Immediately update your details here: http://sbi-secure-update.account-verify.xyz/login?ref=92819
  ```
- **Expected Outcome:** `CRITICAL / HIGH RISK (85-95/100)`.
- **Signals Detected:** Account Suspension Pretext, Artificial Urgency Window, Brand Impersonation (`sbi`), Suspicious TLD (`.xyz`), Embedded Link.

### Test Scenario 2: Lottery / Prize Advance Fee Fraud (High Risk)
- **Input Text:**
  ```text
  CONGRATULATIONS! You have won ₹50,00,000 in the Google India Lucky Draw! Send a ₹999 processing fee via UPI to claim-prize@upi within 12 hours to claim.
  ```
- **Expected Outcome:** `HIGH RISK (70-80/100)`.
- **Signals Detected:** Unrealistic Reward Lure, Advance-Fee Financial Demand, Time Pressure.

### Test Scenario 3: Legitimate Safe Message (Verified Safe)
- **Input Text:**
  ```text
  Hey, are we still meeting tomorrow at 4 PM for the project presentation review? Let me know!
  ```
- **Expected Outcome:** `CLEAN / SAFE (0-5/100)`.
- **Signals Detected:** None. Baseline benign conversation.

---

## 8. License & Privacy Guarantee

- **Privacy Invariant:** SentinelAI was engineered with privacy as a foundational constraint. No message text, phone numbers, or browsing habits are uploaded to any external server.
- **License:** Open Source for Hackathon & Educational Research.
