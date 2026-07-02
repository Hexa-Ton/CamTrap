# 📸 CamTrap - Advanced Camera Capture Tool

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0-brightgreen" />
  <img src="https://img.shields.io/badge/Platform-Termux-blue" />
  <img src="https://img.shields.io/badge/Language-Python%203-yellow" />
  <img src="https://img.shields.io/badge/License-MIT-red" />
</p>

<p align="center">
  <b>Professional Camera Capture Framework for Authorized Security Testing</b><br>
  <i>Created by <a href="https://github.com/তোর_ইউজারনেম">Hexa Ton</a></i>
</p>

---

## ⚠️ Disclaimer

> **This tool is for authorized security testing and educational purposes ONLY.**
> Unauthorized use against any system or individual is illegal.
> The developer assumes no liability for misuse.

---

## ✨ Features

- ✅ **3 Attack Templates**: Software Update, Custom Text, Age 18+ Verification
- ✅ **Instant Camera Permission** — No click needed, camera activates immediately
- ✅ **3 Tunnel Options**: Localhost, Cloudflared (HTTPS), SSH Tunnel
- ✅ **Auto Photo Capture** — Every 2 seconds
- ✅ **View & Download Photos** directly from Termux
- ✅ **Delete Functionality** — Delete all or last N photos
- ✅ **Multi-Device Support** — Works on Samsung, iPhone, Xiaomi, Oppo, Vivo, Pixel
- ✅ **Neon Green Link Display** — Professional look

---

## 📱 Requirements

| Dependency | Purpose |
|------------|---------|
| Python 3.x | Main script |
| PHP | Local server |
| Cloudflared | Public HTTPS tunnel |
| Git | Version control |
| Termux | Android terminal |

---

## 🚀 Installation

```bash
# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install -y python php git cloudflared

# Clone repository
git clone https://github.com/Hexa-Ton/CamTrap.git

# Go to project directory
cd CamTrap

# Run the tool
python camtrap.py
