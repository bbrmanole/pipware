<h1 align="center">
  Pipware
  <br>
</h1>

<h4 align="center">Simple Python program / firmware to run a Raspberry Pi as a Fallout PipBoy.</h4>
<p align="center">
  <a href="https://raspberrypi.com">
    <img src="https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi"
         alt="Gitter">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"
         alt="Gitter">
<p align="center">
  <a href="https://github.com/bbrmanole/pipware">
    <img src="https://img.shields.io/badge/Contributions-Welcome-blue?style=for-the-badge&logo=github&logoColor=white"
         alt="Gitter">
         

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#hardware-requirements">Hardware Requirements</a> •
  <a href="#instructions">Instructions</a> •
  <a href="#credits">Credits</a> •
  <a href="#to-do">To Do</a> •
  <a href="#license">License</a> •
</p>
<p align="center">
<img width="484" height="358" alt="image" src="https://github.com/user-attachments/assets/fe35be22-0e95-4d65-b598-082783895845" />


# Key Features

* 🗓️ Calendar Function
  - View the calendar (current date)
* 🕔 Current Time
* 🗒️ Personal Notes
  - Write, check and delete notes
* ⌨️ On-Screen keyboard (matchbox-keyboard: https://github.com/Xlab/matchbox-keyboard)
* 🔊 Music Player (in development, contributions welcome)

# Hardware Requirements
This project was designed to create a portable and functional Pipboy device. For this, you will need:
* #### A Raspberry Pi 4 or higher rev
  - [![Visit Site - Raspberry Pi](https://img.shields.io/badge/Visit_Site-Raspberry_Pi-red?logo=raspberrypi&logoColor=white)](https://raspberrypi.com/ "Go To Raspberry Pi Homepage")
  - [![RPi Imager - RaspberryPiOS](https://img.shields.io/badge/RPi_Imager-RaspberryPiOS-red?logo=raspberrypi&logoColor=white)](https://raspberrypi.com/software/ "Go to Raspberry Pi Software Page")
* #### TFT Touchscreen 2.8in 480x360 display
  - [![Repo - TFT Display Driver](https://img.shields.io/badge/Repo-TFT_Display_Driver-blue?logo=github&logoColor=white)](https://github.com/goodtft/LCD-show/ "Go To LCD-show Repository Page")

* A stylus (usually comes with the display)

### The wiring diagram can be found here:
[![TFT display information - lcdwiki.com](https://img.shields.io/badge/TFT_display_information-lcdwiki.com-lightgrey)](https://www.lcdwiki.com/2.8inch_RPi_Display/ "lcdwiki.com/2.8inch_RPi_Display")

# Instructions
## Hardware:
### Notice: wiring a touchscreen display is not necessary, since the program will run on any display with a pointing device (mouse or stylus). Use a touchscreen display if you want to make the RaspberryPi portable. If you are going to use a display check out the <a href="#hardware-requirements">Hardware Requirements</a> and follow the steps below:

* ### 1. Follow the wiring diagram (see <a href="#hardware-requirements">Hardware Requirements</a>)


* ### 2. After wiring the display to the Pi, you will need to install an LCD driver. We recommend the LCD-show driver packages from goodtft on GitHub (see <a href="#hardware-requirements">Hardware Requirements</a> or [click here](https://github.com/goodtft/LCD-show/ "Go to LCD-show repository page"))

* ### 3. After installing the LCD display driver and ensuring the touchscreen works as intended, you can move on to the software section

## Software:

### Before installing the firmware, you'll need to install RaspberryPiOS onto your RaspberryPi. Use a microSD card for best results, and follow the instructions on the official RaspberryPi website, which you can find [here](https://raspberrypi.com/software/ "Download Page for the RaspberryPi Imager") or click the badge below:
[![RPi Imager - RaspberryPiOS](https://img.shields.io/badge/RPi_Imager-RaspberryPiOS-red?logo=raspberrypi&logoColor=white)](https://raspberrypi.com/software)

### A bash install wizard script is provided in the repository files, as this project uses multiple Python dependencies that need to be installed for it to work ([requirements file](https://github.com/bbrmanole/pipware/blob/main/requirements.txt)).
### Notice: this program was only tested on the RaspberryPiOS, for best results execute the following instructions on the Raspberry Pi.
To install and use write the following in the terminal:

## 1. Clone this repository:
```bash
$ git clone https://github.com/bbrmanole/pipware
```

## 2. Go into the directory:
```bash
$ cd pipware
```

## 3. Run the install script (this will install all required dependencies, requires root privileges):
```bash
$ sudo ./install.sh
```

## 4. Run the firmware:
```bash
$ python3 main.py
```

# Credits

Thank you to my friends for contributing to make this project what it is today, check out their pages below:

- [![GitHub - FIAX](https://img.shields.io/badge/GitHub-FIAX-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/axente-filip)
- [![GitHub - EncrustedPhantom](https://img.shields.io/badge/GitHub-EncrustedPhantom-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/encrustedphantom)



# Support

## If you like this project, consider forking and contributing to make it better and more feature packed! (before contributing, please see the [contribution guidelines](https://github.com/bbrmanole/pipware/blob/main/CONTRIBUTIONS.md))

If you can't be asked to contribute but still want to support, you can buy me a coffee here:

[![bbrmanole - Buy Me A Coffee](https://img.shields.io/badge/bbrmanole-Buy_Me_A_Coffee-yellow?style=for-the-badge&logo=buymeacoffee&logoColor=white)](https://buymeacoffee.com/bbrmanole)

# To Do
* ### Add a comprehensive documentation
* ### Add more features (e.g. GPS)
* ### Add a startup script to enable the program to launch on RaspberryPi Startup
* ### Add .deb and .rpm packages to assets
* ### Fix issues
* ### Refined installer wizard
* ### Revamp the music player
* ### Revamp de ui

## Contributions welcome and appreciated!

# License
  ### This project uses the GNU General Public License v3.0
  
  [![License - GPL 3.0](https://img.shields.io/badge/License-GPL_3.0-lightgrey?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0.en.html)

---

> dev website coming soon! &nbsp;&middot;&nbsp;
> GitHub Contributors:  [@bbrmanole](https://github.com/bbrmanole) &nbsp;&nbsp;
> [@FIAX](https://github.com/axente-filip) &nbsp;&nbsp;
> [@encrustedphantom](https://github.com/encrustedphantom) &nbsp;&nbsp;


