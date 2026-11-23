
# 🔒 SecureFlow - DevSecOps Security Scanner

> Automated multi-scanner vulnerability detection for CI/CD pipelines with web dashboard

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)
![Security](https://img.shields.io/badge/Security-DevSecOps-green?style=flat-square)
![Scanners](https://img.shields.io/badge/Scanners-3%20Integrated-orange?style=flat-square)
![Findings](https://img.shields.io/badge/Detects-32+%20Issues-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square)

---

## 🎯 Overview

**SecureFlow** is a comprehensive DevSecOps security scanning orchestrator that integrates multiple industry-standard security tools into a unified platform. It detects vulnerabilities in source code, dependencies, and secrets, presenting findings through both a beautiful CLI and an interactive web dashboard.

### 🌟 Why SecureFlow?

Most security tools work in isolation. SecureFlow orchestrates them all:
```
Your Code → SecureFlow → Semgrep (Code Analysis)
                      → Trivy (Dependencies)
                      → TruffleHog (Secrets)
                      → Unified Report + Dashboard
```

---

## 🚀 Features

### Core Scanning
- 🔍 **SAST** - Semgrep static code analysis
- 📦 **SCA** - Trivy dependency vulnerability scanning
- 🔑 **Secret Detection** - TruffleHog git history scanning
- 📊 **Unified Reporting** - Aggregated results from all scanners
- 💾 **JSON Export** - Machine-readable results for CI/CD

### Web Dashboard
- 🌐 **Interactive Dashboard** - Beautiful web interface
- 📈 **Visual Charts** - Severity and scanner breakdown
- 🎨 **Modern UI** - Clean, responsive design
- 📋 **Detailed Reports** - Vulnerability details view

### CLI Interface
- 🎨 **Colored Output** - Color-coded severity indicators
- 📂 **Smart Categorization** - By type and severity
- 🔧 **Flexible Options** - Run individual or all scanners

---

## 📊 Detection Capabilities

| Category | Tool | Severity |
|----------|------|----------|
| **Code Injection** | Semgrep | 🔴 Critical |
| **SQL Injection** | Semgrep | 🔴 Critical |
| **Command Injection** | Semgrep | 🔴 Critical |
| **XSS** | Semgrep | 🔴 Critical |
| **Hardcoded Secrets** | Semgrep + TruffleHog | 🔴 Critical |
| **Path Traversal** | Semgrep | 🟠 High |
| **Vulnerable Dependencies** | Trivy | 🟠 High |
| **Weak Cryptography** | Semgrep | 🟡 Medium |
| **Security Misconfig** | Semgrep | 🟡 Medium |
| **Template Injection** | Semgrep | 🔴 Critical |

---

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/Kali-ai007/SecureFlow.git
cd SecureFlow

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify all tools
python3 cli/main.py check
```

### CLI Usage
```bash
# Check tools
python3 cli/main.py check

# Scan with Semgrep (code analysis)
python3 cli/main.py scan -t /path/to/project -s semgrep

# Scan with Trivy (dependencies)
python3 cli/main.py scan -t /path/to/project -s trivy

# Scan with TruffleHog (secrets)
python3 cli/main.py scan -t /path/to/project -s trufflehog

# Run ALL scanners with unified report
python3 cli/main.py scan -t /path/to/project -s all

# Show all findings
python3 cli/main.py scan -t /path/to/project -s all --all
```

### Web Dashboard
```bash
# Start dashboard
python3 dashboard/app.py

# Open browser
# http://localhost:5000
```

---

## 📊 Example Output
```
╔═══════════════════════════════════════════════════════╗
║              🔒 SECUREFLOW v2.0 🔒                   ║
║     Your DevSecOps Security Scanner Orchestrator     ║
║              Now with 3 Integrated Scanners!         ║
╚═══════════════════════════════════════════════════════╝

================================================================================
📊 SECUREFLOW UNIFIED SECURITY REPORT
================================================================================

🕐 Scan Time: 2026-02-16T16:24:05
🔧 Scanners Used: Semgrep, Trivy, TruffleHog

📈 OVERALL SUMMARY:
   Total Security Findings: 32

🎯 By Severity:
   🔴 CRITICAL: 12
   🟠 HIGH:     2
   🟡 MEDIUM:   18
   🟢 LOW:      0

🔍 By Scanner:
   Semgrep (SAST): 27 findings
   Trivy (SCA): 4 findings
   TruffleHog (Secrets): 1 finding

💡 RECOMMENDATIONS:
   ⚠️  12 CRITICAL issues require IMMEDIATE attention!
   🟠 2 HIGH severity issues should be fixed soon
   🟡 18 MEDIUM issues - plan to address
================================================================================
```

---

## 🏗️ Project Structure
```
SecureFlow/
├── cli/
│   └── main.py                      # CLI interface
├── scanners/
│   ├── semgrep_scanner.py           # SAST scanning
│   ├── trivy_scanner.py             # Dependency scanning
│   └── trufflehog_scanner.py        # Secret detection
├── aggregator/
│   └── result_aggregator.py         # Unified reporting
├── dashboard/
│   ├── app.py                       # Flask web server
│   ├── templates/dashboard.html     # Web UI
│   └── static/css/style.css         # Styling
├── data/scans/                      # JSON results
├── docs/LEARNING_LOG.md             # Dev journey
├── test-apps/
│   ├── vulnerable-app/              # Insecure examples
│   └── secure-example/              # Secure examples
└── requirements.txt
```

---

## 📈 Development Journey

### Day 1 - Foundation
- Environment setup (Kali Linux, Python, tools)
- Project structure and architecture
- Tool verification

### Day 2 - Core Scanner
- Semgrep SAST integration
- CLI tool with colored output
- Found 27 vulnerabilities in test app!

### Day 3 - Multi-Scanner
- Trivy dependency scanner
- TruffleHog secret scanner
- Result aggregator and unified report
- Secure coding examples with encryption
- Total: 32 vulnerabilities detected!

### Day 4 - Web Dashboard
- Flask web server
- Interactive HTML dashboard
- Chart.js visualizations
- Severity and scanner charts
- Recommendations display

---

## 🚧 Roadmap

### Completed
- [x] Semgrep SAST integration
- [x] Trivy SCA integration
- [x] TruffleHog secret detection
- [x] Multi-scanner orchestration
- [x] Unified security report
- [x] Web dashboard with charts
- [x] Secure coding examples
- [x] CLI with colored output

### Planned
- [ ] PDF report generation
- [ ] GitHub Actions integration
- [ ] Docker containerization
- [ ] Auto-fix suggestions
- [ ] Risk scoring algorithm
- [ ] Slack notifications
- [ ] Custom rule creation
- [ ] SARIF format export

---

## 🔒 Security Examples

### Vulnerable Code
```python
# SQL Injection - BAD
sql = f"SELECT * FROM users WHERE name = '{user_input}'"

# Command Injection - BAD
os.system(f'ping -c 1 {user_input}')

# Hardcoded Secret - BAD
API_KEY = "sk_live_abc123"
```

### Secure Code
```python
# SQL Injection prevention
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))

# Command Injection prevention
subprocess.run(['ping', '-c', '1', host], capture_output=True)

# Secrets management
API_KEY = os.getenv('STRIPE_API_KEY')
```

---

## 🎯 CI/CD Integration
```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run SecureFlow
        run: |
          pip install semgrep
          python3 cli/main.py scan -t . -s all
```

---

## 📊 Statistics

| Metric | Value |
|--------|-------|
| Lines of Code | 1,800+ |
| Files Created | 20+ |
| Scanners | 3 |
| Vulnerabilities Detected | 32 |
| Development Days | 4 |
| Commits | 9+ |

---

## 🛡️ Security Notice

The test-apps/vulnerable-app/ directory contains intentionally vulnerable
code for educational purposes. All API keys are FAKE test data.
See test-apps/secure-example/ for proper security practices.

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit: `git commit -m 'Add AmazingFeature'`
4. Push: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 📝 License

MIT License - Copyright (c) 2026 Kushal Rayamajhi

---

## 👨‍💻 Author

**Kushal Rayamajhi** - Security Enthusiast & Developer
- GitHub: [@Kali-ai007](https://github.com/Kali-ai007)
- Project: [SecureFlow](https://github.com/Kali-ai007/SecureFlow)

---

## 🙏 Acknowledgments

- Semgrep, Trivy, TruffleHog teams
- OWASP for security resources
- Chart.js for visualizations
-
<img width="657" height="806" alt="Screenshot 2026-02-16 231544" src="https://github.com/user-attachments/assets/a2a1287a-bac3-4599-9e55-b8999b9bbdac" />
<img width="698" height="850" alt="Screenshot 2026-02-16 230825" src="https://github.com/user-attachments/assets/bb2abe22-60ae-45f5-ae3b-0ebf736f66d8" />
<img width="670" height="833" alt="Screenshot 2026-02-16 230818" src="https://github.com/user-attachments/assets/42da88e2-d805-4e7b-9ede-fef4ddad59ca" />
<img width="647" height="822" alt="Screenshot 2026-02-16 230811" src="https://github.com/user-attachments/assets/9968b096-4ec0-4bfe-8bbd-7f49791682fa" />


---

⭐ Star this repo if you found it useful!

*Built with ❤️ over 4 intensive days of learning DevSecOps*
