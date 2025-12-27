# 🚀 PDF Architect Pro

<p align="center">
  <img src="https://img.shields.io/badge/Version-v11.2-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-purple?style=for-the-badge" alt="Platform">
</p>

<p align="center">
  <b>A powerful, ethical, and feature-rich PDF compression & management tool</b>
</p>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛡️ Ethical Security Policy](#️-ethical-security-policy)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [⚙️ Configuration Options](#️-configuration-options)
- [📊 Compression Levels](#-compression-levels)
- [📝 Logging](#-logging)
- [🤝 Contributing](#-contributing)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗜️ **Smart Compression** | Three levels of compression (Low, Mid, High) using AES-256 encryption |
| 🔐 **Password Management** | Keep, remove, or set new passwords on PDFs |
| 📝 **Metadata Editor** | Inject custom title, author, and keywords into PDFs |
| 📊 **Progress Visualization** | Beautiful animated progress bar during processing |
| 📁 **Auto Folder Open** | Automatically opens output folder after completion |
| 📋 **Operation Logging** | Detailed logs saved to `pdf_architect.log` |
| 🎨 **Colorful CLI** | Beautiful terminal UI with colors and animations |
| 🔄 **Unique Naming** | Auto-generates unique filenames to prevent overwrites |
| 💻 **Cross-Platform** | Works on Windows, macOS, and Linux |

---

## 🛡️ Ethical Security Policy

```
✔ Passwords are NEVER cracked or bypassed
✔ Only user-provided passwords are accepted
✔ Use only files you own or have permission for
⚖ This tool respects PDF encryption standards
```

> **Note:** This tool is designed with ethics in mind. It will not attempt to break or bypass any PDF security measures.

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/SudhirDevOps1/pdf-architect-pro.git
cd pdf-architect-pro
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install PyMuPDF colorama
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `PyMuPDF` (fitz) | PDF manipulation and compression |
| `colorama` | Cross-platform colored terminal output |

---

## 🚀 Usage

### Run the Application

```bash
python pdf_architect.py
```

### Interactive Workflow

1. **Enter PDF Path** - Provide the full path to your PDF file
2. **Password Prompt** - If PDF is encrypted, enter the password
3. **Set Metadata** - Customize title, author, and keywords
4. **Password Options** - Choose to keep, remove, or set new password
5. **Compression Level** - Select Low, Mid, or High compression
6. **Done!** - Output file is saved and folder opens automatically

### Quick Example

```
📂 Enter PDF Path ➜ /path/to/document.pdf

🔍 PDF Security Report
• Originally Encrypted : NO
• Currently Locked     : NO
• Page Count           : 25

🧾 Metadata Injector
Title ➜ My Document
Author ➜ John Doe
Keywords ➜ report, annual, 2024

🔐 Password-protect output? (y/n) ➜ n

🗜 Compression Level
[1] Low
[2] Mid
[3] High
Select ➜ 2

📄 Processing Pages [████████████████████] 25/25

✅ SUCCESSFUL!
📍 Path ➜ /path/to/document_compressed.pdf
Before ➜ 15.20 MB
After  ➜ 8.45 MB
Saved  ➜ 44.4%
```

---

## ⚙️ Configuration Options

### Password Management Options

| Option | Description |
|--------|-------------|
| **Keep Original** | Maintains the same password as the source PDF |
| **Remove Password** | Creates an unprotected output PDF |
| **Set New Password** | Applies a new password with AES-256 encryption |

### Metadata Fields

| Field | Default Value |
|-------|---------------|
| Title | Original filename |
| Author | "Sudhir Singh" |
| Keywords | "PDF, Compression" |
| Creator | "Sudhir Singh - PDF Architect Pro" |
| Producer | "SudhirDevOps1" |

---

## 📊 Compression Levels

| Level | Garbage Collection | Best For |
|-------|-------------------|----------|
| 🟢 **Low** | Level 2 | Quick compression, minimal quality loss |
| 🟡 **Mid** | Level 3 | Balanced compression and quality |
| 🔴 **High** | Level 4 | Maximum compression, smaller file size |

> **Tip:** For documents with many images, High compression yields the best results.

---

## 📝 Logging

All operations are logged to `pdf_architect.log` with the following information:

```
[2024-01-15 14:30:25.123456]
Input  : /path/to/original.pdf
Output : /path/to/original_compressed.pdf
Pages  : 25
Saved  : 44.4%
----------------------------------------
```

---

## 🖥️ System Requirements

| OS | Supported |
|----|-----------|
| Windows 10/11 | ✅ |
| macOS 10.14+ | ✅ |
| Ubuntu 18.04+ | ✅ |
| Other Linux | ✅ |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 👨‍💻 Author

<p align="center">
  <b>Sudhir Singh</b><br>
  <a href="https://github.com/SudhirDevOps1">
    <img src="https://img.shields.io/badge/GitHub-@SudhirDevOps1-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Sudhir Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/SudhirDevOps1">Sudhir Singh</a>
</p>

<p align="center">
  ⭐ Star this repo if you find it helpful!
</p>
