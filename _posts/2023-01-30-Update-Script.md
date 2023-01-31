---
title: Update Script
date: 2023-01-30 10:31:00
categories: [Scripts, Bash]
tags: [bash, scripts]
---

As I tend to have things installed though multiple package managers on my Linux installs I created this scripts to update them all. It will update then upgrade the apt packages, then update the snap packages, then update the flatpaks, and then run an autoclean and autoremove. I added headers so its easy to see what part it is doing.

This is what it looks like when run:  
![](https://raw.githubusercontent.com/ben-hodgson/things/main/update_screenshot.png){: .normal w="534" h:"881"}

This is the script for it:  
```bash
#!/bin/bash
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'
BOLD=$(tput bold)
NORM=$(tput sgr0)
sudo rm -rf /var/lib/dpkg/lock-frontend
sudo rm -rf /var/liv/dpkg/lock
echo -e "${YELLOW}***************${NC}"
echo -e "${RED}${BOLD}Update Packages${NC}${NORM}"
echo -e "${YELLOW}***************${NC}"
echo ""
sudo apt update
echo ""
echo -e "${YELLOW}****************${NC}"
echo -e "${RED}${BOLD}Upgrade Packages${NC}${NORM}"
echo -e "${YELLOW}****************${NC}"
echo ""
sudo apt upgrade -y
echo ""
echo -e "${YELLOW}*********************${NC}"
echo -e "${RED}${BOLD}Refresh Snap Packages${NC}${NORM}"
echo -e "${YELLOW}*********************${NC}"
echo ""
sudo snap refresh
echo ""
echo -e "${YELLOW}************************${NC}"
echo -e "${RED}${BOLD}Update Flatpack Packages${NC}${NORM}"
echo -e "${YELLOW}************************${NC}"
echo ""
sudo flatpak update -y
echo ""
echo -e "${YELLOW}***************${NC}"
echo -e "${RED}${BOLD}Upgrade Distro${NC}${NORM}"
echo -e "${YELLOW}***************${NC}"
echo ""
sudo apt-get dist-upgrade -y
echo ""
echo -e "${YELLOW}*******************${NC}"
echo -e "${RED}${BOLD}Autoremove Packages${NC}${NORM}"
echo -e "${YELLOW}*******************${NC}"
echo ""
sudo apt autoremove -y
echo ""
echo -e "${YELLOW}******************${NC}"
echo -e "${RED}${BOLD}Autoclean Packages${NC}${NORM}"
echo -e "${YELLOW}******************${NC}"
echo ""
sudo apt autoclean -y
```

I named it `update` and moved it into the `/usr/bin` folder so I only have to input update in the cli and it will run all of them together.