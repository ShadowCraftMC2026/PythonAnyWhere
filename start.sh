#!/bin/bash

git clone https://github.com/ShadowCraftMC2026/PythonAnyWhere
cd /root/ShadowCraft2026/PythonAnyWhere
sudo apt update && sudo apt upgrade -y
sudo apt install python3
sudo apt install pip3
pip3 install -r requirements.txt
python3 app.py
