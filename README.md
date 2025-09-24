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
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## Key Features

* 🗓️ Calendar Function
  - View the calendar (current date)
* 🕔 Current Time
* 🗒️ Personal Notes
  - Write, check and delete notes
* ⌨️ On-Screen keyboard (matchbox-keyboard: https://github.com/Xlab/matchbox-keyboard)
* 🔊 Music Player (in development, contributions welcome)

## Hardware Requirements
This project was designed to create a portable and functional Pipboy device. For this, you will need:
* #### A Raspberry Pi 4 or higher rev
  - [![Visit Site - Raspberry Pi](https://img.shields.io/badge/Visit_Site-Raspberry_Pi-red?logo=raspberrypi&logoColor=red)](https://raspberrypi.com/ "Go To Raspberry Pi Homepage")

* #### TFT Touchscreen 2.8in 480x360 display
  - [![Repo - TFT Display Driver](https://img.shields.io/badge/Repo-TFT_Display_Driver-blue?logo=github&logoColor=white)](https://github.com/goodtft/LCD-show/ "Go To LCD-show Repository Page")

* A stylus (usually comes with the display)

### The wiring diagram can be found here:
[![TFT display information - lcdwiki.com](https://img.shields.io/badge/TFT_display_information-lcdwiki.com-lightgrey)](https://www.lcdwiki.com/2.8inch_RPi_Display/ "lcdwiki.com/2.8inch_RPi_Display")

## How To Use

### A bash install wizard script is provided in the repository files, as this project uses multiple Python dependencies that need to be installed for it to work (requirements.txt).
### Notice: this program was only tested on the RaspberryPiOS, for best results execute the following instructions on the raspberrypi
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

## Credits

Thank you to my friends for contributing to make this project what it is today, check out their pages below:

- [![GitHub - FIAX](https://img.shields.io/badge/GitHub-FIAX-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/axente-filip)
- [![GitHub - EncrustedPhantom](https://img.shields.io/badge/GitHub-EncrustedPhantom-blue?style=for-the-badge&logo=github&logoColor=white)](https://github.com/encrustedphantom)



## Support

### If you like this project, consider forking and contributing to make it better and more feature packed!

If you can't be asked to contribute but still liked the project, you can buy me a coffee here:

[![bbrmanole - Buy Me A Coffee](https://img.shields.io/badge/bbrmanole-Buy_Me_A_Coffee-yellow?style=for-the-badge&logo=buymeacoffee&logoColor=white)](https://buymeacoffee.com/bbrmanole)


## License

  [![License - GPL 3.0](https://img.shields.io/badge/License-GPL_3.0-lightgrey?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0.en.html)

---

> dev website coming soon! &nbsp;&middot;&nbsp;
> GitHub Contributors:  [@bbrmanole](https://github.com/bbrmanole) &nbsp;&nbsp;
> [@FIAX](https://github.com/axente-filip) &nbsp;&nbsp;
> [@encrustedphantom](https://github.com/encrustedphantom) &nbsp;&nbsp;


