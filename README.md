# RaspberryPi PipBoy Firmware
A simple Python 3 firmware script to run a Raspberry Pi as a PDA in the style of the Fallout PipBoy

## Description:

The firmware functions using 3 files: MainMenuScript.py, Applets.py and notes.txt

The notes file keeps track of the user's personal notes (basically a notepad file), the rest are functional code scripts

## Notice:
The use of the firmware requires additional libraries and packages for the Raspberry Pi, the most important one being a keyboard app, since
a function of the script is to launch a virtual keyboard, since this firmware is designed to run on a TFT Touchscreen 2.8in 480x360 display.

You can use either matchbox-keyboard or Onboard, further versions will update the main menu based on which keyboard you prefer.

