#!/bin/bash

loading(){
while true; do for X in '-' '/' '|' '\'; do echo -en "\r$1 $X"; sleep 0.1; done; done 

}

loading_message(){
    loading "$1" &
    loading_pid=$!
    eval "$2" > /dev/null 2>&1 &
    update_pid=$!
    wait $update_pid
    kill $loading_pid

}

yes_or_no(){
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 1  ;;  
            [Nn]*) return  0 ;;
        esac
    done
}


if [[ $EUID -ne 0 ]]; then
  echo "Error: This script requires root privileges. Please run as sudo."
exit 1
fi

echo -e "-| Welcome to the installer wizard for the PipBoy RaspberryPi Firmware! |-\n"
sleep 3s

cat << EOF

This wizard is designed to smooth out the installation process by
automating every installation procedure into a shell script.

The wizard will update the system packages, then install python3 and pip.
After that, it will create a venv in the cloned repo's directory called
'pipwarevenv', it will activate it and then install the necessary dependencies
there.

For more information, please visit the GitHub page at the following link
'https://github.com/manole-55/pipware.git'


EOF

if yes_or_no "Do you wish to proceed with installation?"; then
    exit;
fi

loading_message "Proceeding with installation" "sleep 1.5s"

echo -e "\nUpdating package list...\n"
sleep 1s
sudo apt update
echo -e "\nUpgrading package list...\n"
sleep 1s
sudo apt upgrade
echo -e "\nSystem updates performed\n"
sleep 1.5s

echo -e "\n"
loading_message "Installing python3" "sudo apt install python3"
echo -e "\n"
loading_message "Installing pip" "sudo apt install python3-pip"
echo -e "\n"
loading_message "Creating a venv in current directory" "python3 -m venv pipwarevenv"
echo -e "\n"
loading_message "Activating 'pipwarevenv'" "sleep 1.5s"
echo -e "\n"

source pipwarevenv/bin/activate
pip install -r requirements.txt

echo -e "\n\nInstallation complete!"

if yes_or_no "Would you like to install the 'matchbox-keyboard' system package?"; then
    if yes_or_no "Would you like to run the firmware now?"; then
        loading_message "Closing installer" "sleep 1s"
        echo -e "\n"
        exit;
    else
        python3 main.py
    fi
else
    sudo apt-get install matchbox-keyboard
    if yes_or_no "Would you like to run the firmware now?"; then
        loading_message "Closing installer" "sleep 1s"
        echo -e "\n"
        exit;
    else
        python3 main.py
    fi
fi






