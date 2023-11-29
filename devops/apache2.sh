#!/bin/bash
# become the root user or use sudo
# ubuntu server

sudo apt update
sudo apt install apache2
sudo systemctl status apache2
sudo systemctl status apache2
sudo systemctl enable apache2
sudo ufw allow 'Apache Full'
Sudo systemctl restart apache2 
