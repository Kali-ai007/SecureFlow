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
