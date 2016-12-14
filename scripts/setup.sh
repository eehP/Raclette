#!/bin/bash
#######################################################################
#
#  Project......: raclette_install.sh
#  Description..: Script to install raclette and its depends
#
######################################################################
# Language :
#               bash
# Version : 0.1
#

if [[ $(uname) != 'Linux' && $(arch) != 'x86_64' ]]; then
    echo "This script is only for Linux 64 bits"
    exit 1
fi

if [[ "$(whoami)" != "root" ]]; then
    echo "Please run this script as root"
    exit 1
fi

# Easiest way is to modify this var
stuff_to_install="git nmap make gcc python3"

if [[ $(which apt-get) ]]; then
	apt-get update && apt-get upgrade
	apt-get -y install $stuff_to_install

elif [[ $(which dnf) ]]; then
	dnf install -y $stuff_to_install
else
	echo "No package manager found, exiting..."
	exit 1
fi

# Cloning and installing sysnet <3
if [[ ! -e sysnet ]]
	git clone https://github.com/matteyeux/sysnet
	cd sysnet && make install
else 
	cd sysnet
	git pull
	make install 	# The script is still running as root, no need to run sudo
fi
