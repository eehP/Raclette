#!/bin/bash
# Script to make a deb of Raclette
# To install : sudo dpkg -i raclette.deb

if [[ ! $(which dpkg-deb) ]]; then
	echo "dpkg-deb not found"
	echo "Aborting"
	exit 1
fi

cd ..
mkdir -p deb/usr/local/bin deb/DEBIAN
chmod +x *.py
cp *.py deb/usr/local/bin/
cp resources/control deb/DEBIAN
dpkg-deb --build deb raclette.deb
