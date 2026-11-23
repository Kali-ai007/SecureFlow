# 🚀 SecureFlow Quick Start Guide

## 1️⃣ Install (One Command)
```bash
./install.sh

# 🚀 SecureFlow Quick Start Guide

## 1️⃣ Install (One Command)
```bash
./install.sh
```

That's it! Everything is installed automatically.

---

## 2️⃣ Run Your First Scan
```bash
./secureflow scan -t test-apps/vulnerable-app -s all
```

This will:
- ✅ Scan code for vulnerabilities (Semgrep)
- ✅ Check dependencies for CVEs (Trivy)
- ✅ Find leaked secrets (TruffleHog)
- ✅ Generate unified report

---

## 3️⃣ View Results in Dashboard
```bash
./secureflow-dashboard
```

Your browser will open automatically to: http://localhost:5000

You'll see:
- 📊 Beautiful charts
- 🎯 Severity breakdown
- 💡 Smart recommendations
- 📈 Scanner comparisons

---

## 4️⃣ Scan Your Own Project
```bash
./secureflow scan -t /path/to/your/project -s all
```

Example:
```bash
./secureflow scan -t ~/my-app -s all
```

---

## 🎯 Common Commands

| Command | What it does |
|---------|-------------|
| `./secureflow check` | Verify all tools installed |
| `./secureflow scan -t . -s semgrep` | Scan code only |
| `./secureflow scan -t . -s trivy` | Scan dependencies only |
| `./secureflow scan -t . -s all` | Run all scanners |
| `./secureflow scan -t . -s all --all` | Show ALL findings |
| `./secureflow-dashboard` | Open web dashboard |

---

## 💡 Pro Tips

### Scan current directory
```bash
./secureflow scan -t . -s all
```

### Save results
Results auto-save to: `data/scans/`

### View detailed findings
```bash
./secureflow scan -t . -s all --all
```

### Refresh dashboard
Just press the "🔄 Refresh" button in the web UI!

---

## 🐛 Troubleshooting

**Dashboard shows "No Data"?**
- Run a scan first: `./secureflow scan -t test-apps/vulnerable-app -s all`
- Refresh the browser

**Command not found?**
- Make sure you're in the SecureFlow directory
- Run: `chmod +x secureflow secureflow-dashboard`

**Tools missing?**
- Run: `./install.sh` again

---

## 📚 Need Help?

- 📖 Full docs: `README.md`
- 🐛 Issues: https://github.com/Kali-ai007/SecureFlow/issues
- 💬 Discussions: GitHub Discussions

---

**That's it! You're ready to scan! 🎉**
