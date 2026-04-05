
<h1 align="center" style="font-size: 10em; margin: 2em 0;">
  Netspector
</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=flat&logo=python">
  <img src="https://img.shields.io/github/stars/Red-Warrior-hkg/Netspector?style=flat&logo=github">
  <img src="https://img.shields.io/github/license/Red-Warrior-hkg/Netspector?style=flat">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=flat&logo=python">
  <img src="https://img.shields.io/badge/networking-✓-brightgreen?style=flat">
  <img src="https://img.shields.io/badge/network--scanner-✓-success?style=flat">
  <img src="https://img.shields.io/badge/cybersecurity-✓-red?style=flat">
  <img src="https://img.shields.io/badge/port--scanner-✓-orange?style=flat">
  <img src="https://img.shields.io/badge/CLI-✓-blueviolet?style=flat">
  <img src="https://img.shields.io/badge/network--tools-✓-lightgrey?style=flat">
  <img src="https://img.shields.io/badge/subnet--scan-✓-yellow?style=flat">
  <img src="https://img.shields.io/badge/UDP--scan-✓-blue?style=flat">
  <img src="https://img.shields.io/badge/TCP--scan-✓-blue?style=flat">
  <img src="https://img.shields.io/badge/host--discovery-✓-informational?style=flat">
  <img src="https://img.shields.io/badge/ethical--hacking-✓-critical?style=flat">
  <img src="https://img.shields.io/badge/learning--python-✓-brightgreen?style=flat">
  <img src="https://img.shields.io/badge/penetration--testing-✓-orange?style=flat">
  <img src="https://img.shields.io/badge/network--automation-✓-blue?style=flat">
  <img src="https://img.shields.io/badge/netspector-v1.3-cyan?style=flat">
</p>

<p align="center">
  A lightweight network inspection tool built from scratch for learning and experimentation.
</p>

---

## 📖 Overview

**Netspector** is a simple command-line tool for basic network reconnaissance.  
It focuses on core networking concepts while staying fast, minimal, and dependency-free.

**Use it for:**
- Learning networking fundamentals  
- Understanding how scanners work  
- Practicing Python  
- Building your cybersecurity portfolio  

---

## 🚀 Features

- TCP port scanning (single / range)  
- Basic UDP scanning  
- Host reachability (ping)  
- RTT (latency) measurement  
- Subnet enumeration (CIDR)  
- Private IP detection  
- Local listening ports discovery  
- Domain resolution  
- Interactive CLI  
- Colored output  
- No external dependencies  

---

## 🗂️ Project Structure

<img width="600" height="286" alt="image" src="https://github.com/user-attachments/assets/035b9b65-cd81-48fb-ad7c-c84bf11eda48" />

## ⚙️ Installation

```bash
git clone https://github.com/Red-Warrior-hkg/Netspector.git
cd Netspector
````

### Requirements

* Python 3.6+
* No additional packages required

---

## 🧑‍💻 Usage

### Interactive Mode

```bash
python main.py
```

Commands:

* `help` → show commands
* `exit` → quit

---

### One-shot Mode

```bash
python main.py <command> [options]
```

---

## 📚 Cheat Sheet
<img width="580" height="572" alt="image" src="https://github.com/user-attachments/assets/9fcbd980-15f6-4a10-8ad5-d53da470654a" />


## ⚙️ How It Works

* **TCP Scan** → Full 3-way handshake
* **UDP Scan** → Packet-based detection
* **Ping** → Uses system commands
* **RTT** → Measures connection time
* **Subnet** → Expands CIDR ranges
* **Listening Ports** → Uses system tools

---

## ⚠️ Limitations

* Uses full TCP connect (no SYN scan)
* UDP scanning may be unreliable
* No OS fingerprinting
* Not intended to replace advanced tools

---

## 🔮 Future Improvements

* Web interface + HTML cheat sheet
* Command explanations & quick reference
* Visual scan output
* Export results (JSON / TXT)

---

## ⭐ Support

If you like this project, consider starring it on GitHub.

<p align="center">
  <a href="https://github.com/Red-Warrior-hkg/Netspector">
    <img src="https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github">
  </a>
</p>
