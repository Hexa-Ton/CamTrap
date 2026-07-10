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
| **Kali Linux & Termux** | Supported platforms |

---

## 🚀 Installation

### 🔴 Kali Linux

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 php git
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
rm cloudflared-linux-amd64.deb
git clone https://github.com/Hexa-Ton/CamTrap.git
cd CamTrap
python3 camtrap.py
```
Note: If Cloudflared installation fails via dpkg, try:


curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
chmod +x cloudflared
sudo mv cloudflared /usr/local/bin/


## 🚀 Installation

### 🟢 Termux (Android)

```bash
pkg update -y && pkg upgrade -y
pkg install -y python php git cloudflared
git clone https://github.com/Hexa-Ton/CamTrap.git
cd CamTrap
python camtrap.py
```
Note: If Cloudflared is not found in Termux default repo:


pkg install -y tur-repo
pkg install -y cloudflared

🎯 Usage Guide


1. Run the tool

cd ~/CamTrap
python camtrap.py

2. Select Template

Option	Template
[1]	🌟 Software Update (iOS 16.5.1 Style)
[2]	📝 Custom Text
[3]	🔞 Age 18+ Verification
[0]	❌ Exit

3. Select Tunnel


Option	Method	Type
[1]	💻 Localhost	HTTP (Same Wi-Fi)
[2]	☁️ Cloudflared	HTTPS (Public)
[3]	🔗 SSH Tunnel	HTTP (Alternative)


4. In-Game Commands


Command	 Action
------   ------
c	 Count captured photos
s	 Save to Downloads
d	 Delete menu
O	 Open photo
q	 Quit server
url	 Show link again


🌐 Tunnel Methods


Method	     Type           Best For
------       ----           --------
Localhost    HTTP           Same device or Wi-Fi
Cloudflared  HTTPS(Public)  Any device, anywhere
SSH Tunnel   HTTP	    When Cloudflared unavailable


📸 Templates


Template	  Description
--------          -----------

Software Update	  iOS 16.5.1 fake update with 35-second progress bar
Custom Text	  Any message with 🎉 emojis, auto font-size
Age 18+	Adult     content style verification page


📁 Project Structure



CamTrap/
├── camtrap.py
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
└── captured_data/
    └── images/

📜 License
This project is licensed under the MIT License.

Made with ❤️ by Hexa Ton

```
