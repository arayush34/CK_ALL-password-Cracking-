#!/bin/bash
echo "ismproject Installer"

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


echo "installing pakeges for ismproject"

# this script tested only garuda linux

if [ pip ]
then 
pip install rarfile==4.0
pip install colorama==0.4.4
pip install msoffcrypto-tool==4.12.0
pip install pdfplumber==0.7.5
pip install chardet==5.1.0


elif [ pip3 ]
then 
pip3 install rarfile==4.0
pip3 install colorama==0.4.4
pip3 install msoffcrypto-tool==4.12.0
pip3 install pdfplumber==0.7.5
pip3 install chardet==5.1.0

else echo "pip and pip3 not installed"
fi

echo "start coping files"
cp ./ismproject.py /usr/bin/ismproject
echo "installetion complete"
echo "starting ismproject"
ismproject

