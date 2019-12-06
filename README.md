# Raspberry Pi Workshop

Python Script
-------------

The file "script.py" contains the test script for the Raspberry Pi workshop

Prerequisites:
Install gpiozero with Python pip installer: 
* for Python 2: `sudo pip install gpiozero`
* for Python 3: `sudo pip3 install gpiozero`

Install gpiozero with Debian package manager: 
* for Python 2: `sudo apt install python-gpiozero`
* for Python 3: `sudo apt install python3-gpiozero`

Installation Python LED-Driver:
* for Python 2: `sudo pip install rpi_ws281x`
* for Python 3: `sudo pip3 install rpi_ws281x`

Installation Benchmark-Tool:
* `sudo apt install sysbench`

Documentation:
* https://github.com/rpi-ws281x/rpi-ws281x-python
* https://www.raspberrypi.org/documentation/usage/gpio/python/README.md
* https://gpiozero.readthedocs.io/
* https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
* https://dordnung.de/raspberrypi-ledstrip/ws2812
* https://github.com/jgarff/rpi_ws281x/blob/master/python/neopixel.py

Node-RED Flow
-------------

The File flow.txt contains the Test Flow for Node-RED for the Raspi Workshop

Prerequisites:
* Install NODE-Red (from Terminal): 
  * By Script (recommended): `bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`
  * By Debian packet manager:
    * Node-RED: `sudo apt install nodered`
    * Node-RED packet manager: `sudo apt install npm`
* Recommended additional Add-ons & Nodes (needed for example flow):
  * Dashboard: `npm install node-red-dashboard`
  * CPU-Usage: `npm install node-red-contrib-cpu` (needed for example flow)
  * Install Adafruit package: `curl -sS get.pimoroni.com/unicornhat | bash`
  * Install LED-Node: `npm install node-red-node-pi-neopixel` 
  * *Alternative: Use "Manage Palette" ("Palette verwalten") in NODE-Red for installing Nodes*

Control service (from Terminal):
* Start service by boot: `sudo systemctl enable nodered.service`
* Start service: `node-red-start`
* Stop service: `node-red-stop`
* Restart service: `node-red-restart`
* Show logs: `node-red-log`

Documentation:
* https://nodered.org/docs/getting-started/raspberrypi
* https://flows.nodered.org/node/node-red-dashboard
* https://flows.nodered.org/node/node-red-node-pi-neopixel
* https://flows.nodered.org/node/node-red-contrib-cpu
