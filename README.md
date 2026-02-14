# 🔒 SecureFlow - DevSecOps Security Scanner

> Automated vulnerability detection for CI/CD pipelines

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)
![Security](https://img.shields.io/badge/Security-DevSecOps-green?style=flat-square)
![Vulnerabilities](https://img.shields.io/badge/Detects-27+%20Types-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🎯 Overview

**SecureFlow** is a comprehensive security scanning orchestrator that automates vulnerability detection in your codebase. Built as a hands-on learning project, it integrates multiple industry-standard security tools and presents findings in a unified, actionable format.

### Why SecureFlow?

- 🚀 **Zero Configuration** - Works out of the box with sensible defaults
- 🎨 **Beautiful CLI** - Color-coded output with severity indicators  
- 📊 **Smart Categorization** - Groups vulnerabilities by type and severity
- 💾 **JSON Export** - Machine-readable results for CI/CD integration
- 🔍 **Multi-Scanner Ready** - Designed to orchestrate multiple security tools
- 📚 **Educational** - Learn about common vulnerabilities through examples

---

## 🐛 Vulnerability Detection

SecureFlow currently detects **27+ vulnerability types** including:

| Category | Examples | Severity |
|----------|----------|----------|
| **Injection Attacks** | SQL Injection, Command Injection, Code Injection | 🔴 Critical |
| **XSS Vulnerabilities** | Reflected XSS, Stored XSS, DOM-based XSS | 🔴 Critical |
| **Secrets Exposure** | API Keys, Passwords, Tokens, Private Keys | 🔴 Critical |
| **Security Misconfigurations** | Debug Mode Enabled, Weak Crypto, Insecure Defaults | 🟡 High |
| **Path Traversal** | Directory Traversal, File Inclusion | 🟡 High |
| **Template Injection** | Server-Side Template Injection (SSTI) | 🔴 Critical |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Git
- pip (Python package manager)

### Installation
```bash
# Clone the repository
git clone https://github.com/kksr1994/SecureFlow.git
cd SecureFlow

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Semgrep (primary scanner)
pip install semgrep

# Verify installation
python3 cli/main.py check
```

### Basic Usage
```bash
# Check if all security tools are installed
python3 cli/main.py check

# Scan a project directory
python3 cli/main.py scan -t /path/to/your/project

# Scan with full output (all findings)
python3 cli/main.py scan -t /path/to/your/project --all

# Scan a single file
python3 cli/main.py scan -t vulnerable_app.py
```

---

## 📊 Example Output
```
╔═══════════════════════════════════════════════════════╗
║              🔒 SECUREFLOW v1.0 🔒                   ║
║     Your DevSecOps Security Scanner Orchestrator     ║
╚═══════════════════════════════════════════════════════╝

🔍 Running Semgrep scan on: test-apps/vulnerable-app
✓ Scan completed! Found 27 findings

================================================================================
📊 SEMGREP SCAN RESULTS
================================================================================

📈 Summary:
   Total Findings: 27
   🔴 ERROR:   12
   🟡 WARNING: 15
   🔵 INFO:    0

📂 By Category:
   SQL Injection: 5
   Code Injection: 4
   XSS: 10
   Secrets: 2
   Command Injection: 2
   Path Traversal: 2
   Security Misconfiguration: 2

🔴 [ERROR] Finding #1
   Rule: generic.secrets.security.detected-stripe-api-key
   File: app.py:15
   Issue: Stripe API Key detected

🔴 [ERROR] Finding #2
   Rule: python.flask.security.injection.tainted-sql-string
   File: app.py:24
   Issue: Detected user input used to manually construct a SQL string...

💾 Results saved to: data/scans/semgrep_scan_20260214_135211.json

⚠️  12 CRITICAL (ERROR) findings require immediate attention!
```

---

## 🏗️ Project Structure
```
SecureFlow/
├── cli/
│   └── main.py                    # Command-line interface
├── scanners/
│   ├── __init__.py
│   └── semgrep_scanner.py         # Semgrep SAST integration
├── aggregator/                    # Multi-scanner result merger (planned)
├── analyzer/                      # Risk scoring engine (planned)
├── educator/                      # Vulnerability explanations (planned)
├── dashboard/                     # Web UI (planned)
├── data/
│   └── scans/                     # JSON scan results
├── docs/
│   ├── README.md
│   └── LEARNING_LOG.md            # Development journey
├── test-apps/
│   └── vulnerable-app/            # Intentionally vulnerable test app
│       ├── app.py                 # Python vulnerabilities
│       ├── vulnerable.js          # JavaScript vulnerabilities
│       └── requirements.txt
├── .gitignore
└── requirements.txt
```

---

## 🛠️ Technologies & Tools

### Core Technologies
- **Python 3.11+** - Primary language
- **Semgrep** - Static Application Security Testing (SAST)
- **JSON** - Result storage and data interchange

### Planned Integrations
- **Trivy** - Container and dependency vulnerability scanning
- **Grype** - Accurate CVE matching
- **TruffleHog** - Git history secret scanning

### Libraries Used
- `argparse` - CLI argument parsing
- `subprocess` - External tool orchestration
- `json` - Data serialization
- `pathlib` - Modern file path handling
- `datetime` - Timestamp generation

---

## 📚 What I Learned

Building SecureFlow was an intensive learning experience covering:

### Security Concepts
✅ OWASP Top 10 vulnerabilities  
✅ SAST vs DAST vs SCA  
✅ CVE databases and severity scoring  
✅ Secret detection patterns  
✅ Secure coding practices  

### Python Development
✅ Object-oriented programming  
✅ Subprocess management  
✅ JSON parsing and manipulation  
✅ CLI tool development  
✅ Error handling and logging  
✅ Virtual environments  

### DevOps & Tools
✅ Git version control  
✅ GitHub workflows  
✅ CI/CD integration concepts  
✅ Security tool orchestration  
✅ Result normalization  

---

## 🎯 Use Cases

### 1. **CI/CD Integration**
```yaml
# .github/workflows/security.yml
- name: Run SecureFlow
  run: |
    python3 cli/main.py scan -t .
```

### 2. **Pre-commit Hook**
```bash
#!/bin/bash
python3 /path/to/SecureFlow/cli/main.py scan -t . || exit 1
```

### 3. **Security Audit**
```bash
# Scan entire codebase and generate report
python3 cli/main.py scan -t /path/to/project --all
```

### 4. **Learning Tool**
Study the `test-apps/vulnerable-app/` to understand common security issues.

---

## 🚧 Roadmap

### ✅ Completed (v1.0)
- [x] Semgrep integration with SAST scanning
- [x] CLI tool with beautiful colored output
- [x] JSON result export
- [x] Vulnerability categorization by severity and type
- [x] Intentionally vulnerable test application

### 🔄 In Progress
- [ ] Trivy scanner for dependency vulnerabilities
- [ ] TruffleHog for git history secret scanning
- [ ] Result aggregator to merge multi-scanner output

### 📋 Planned Features
- [ ] Web dashboard with charts and graphs
- [ ] Auto-fix suggestions for common issues
- [ ] Custom rule creation interface
- [ ] Risk scoring algorithm
- [ ] Docker containerization
- [ ] GitHub Action for easy integration
- [ ] Slack/Discord notifications
- [ ] HTML report generation

---

## 🛡️ Security Notice

⚠️ **IMPORTANT:** This repository contains **intentionally vulnerable code** in the `test-apps/` directory for educational purposes.

- The API keys and secrets are **FAKE** and not connected to any real services
- These files demonstrate what **NOT** to do in production code
- All test secrets have been reviewed and marked as safe in GitHub's security scanning
- **Never use code from `test-apps/` in production!**

---

## 📊 Project Statistics

- **Lines of Code:** 800+
- **Commits:** Multiple with detailed messages
- **Vulnerabilities Detected:** 27 types in test application
- **Scanners Integrated:** 1 (Semgrep), 3 more planned
- **Detection Categories:** 8+ vulnerability classes
- **Development Time:** 2 intensive days of learning

---

## 🤝 Contributing

This is primarily a learning project, but contributions are welcome!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- 🐛 Bug fixes
- 📝 Documentation improvements
- ✨ New scanner integrations
- 🎨 UI/UX enhancements
- 🧪 Additional test cases

---

## 📝 License

This project is licensed under the MIT License - see below for details:
```
MIT License

Copyright (c) 2026 kksr1994

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 👨‍💻 Author

**kksr1994**

- GitHub: [@kksr1994](https://github.com/kksr1994)
- Project Link: [SecureFlow](https://github.com/kksr1994/SecureFlow)

Built as an intensive hands-on learning project to understand:
- DevSecOps principles and practices
- Security automation and tool integration
- Python development and CLI design
- CI/CD security integration

---

## 🙏 Acknowledgments

- **Semgrep** - For their excellent open-source SAST tool
- **OWASP** - For vulnerability classification and educational resources
- **GitHub** - For secret scanning and security features
- The security community for sharing knowledge and best practices

---

## 📖 Learning Resources

If you're interested in learning more about the topics covered:

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Semgrep Documentation](https://semgrep.dev/docs/)
- [DevSecOps Best Practices](https://www.devsecops.org/)
- [Python Security](https://python.readthedocs.io/en/stable/library/security_warnings.html)

---

**⭐ Star this repo if you found it useful for learning!**

**🔗 Share with others interested in DevSecOps and security automation!**

---

*Built with ❤️ and lots of ☕ for learning and education*
