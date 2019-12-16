# Raspberry Pi Workshop

Python Script
-------------

The file `script.py` contains the test script for the Raspberry Pi workshop

**Prerequisites:**
* Wiring:
https://cdn-learn.adafruit.com/assets/assets/000/063/929/original/led_strips_raspi_NeoPixel_bb.jpg?1539981142

* Install Mu-Editor:
  * `sudo apt install mu-editor`
  * *Alternative: Preferences Menu --> Recommended Software --> Mu*
* Install gpiozero 
  * with Python pip installer: 
    * for Python 2: `sudo pip install gpiozero`
    * for Python 3: `sudo pip3 install gpiozero`
  * with Debian package manager (alternative): 
    * for Python 2: `sudo apt install python-gpiozero`
    * for Python 3: `sudo apt install python3-gpiozero`

* Installation Python LED-Driver:
  * for Python 2: `sudo pip install rpi_ws281x`
  * for Python 3: `sudo pip3 install rpi_ws281x`

* Installation Benchmark-Tool:
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

The File `flow.txt` contains the Test Flow for Node-RED for the Raspi Workshop

**Prerequisites:**
* Install NODE-Red (from Terminal): 
  * By Script (recommended): 
    * `bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`
  * By Debian packet manager:
    * Node-RED: `sudo apt install nodered`
    * node.js packet manager: `sudo apt install npm`
    
* Setup Node-RED (from Terminal):
  * Start service by boot: `sudo systemctl enable nodered.service` <-- recommended
  * Start service: `node-red-start`
  * Stop service: `node-red-stop`
  * Restart service: `node-red-restart`
  * Show logs: `node-red-log`
    
* Recommended additional Add-ons & Nodes (needed for example flow):
  * Install in Terminal:
    * Dashboard: `npm install node-red-dashboard`
    * CPU-Usage: `npm install node-red-contrib-cpu` (needed for example flow)
    * Adafruit package (needed for Neopixel-Node): `curl -sS get.pimoroni.com/unicornhat | bash`
    * Neopixel-Node: `npm install node-red-node-pi-neopixel` 
  * Alternative: Install in Node-RED: 
    * Use Menu (right upper edge) --> "Palette verwalten" --> "Installieren"
    * search for:
      * node-red-dashboard
      * node-red-contrib-cpu
      * node-red-node-pi-neopixel
    * and install it.
    * Attention: `curl -sS get.pimoroni.com/unicornhat | bash` is still needed to install in terminal for proper use of WS281x-LEDs

* Import explampe flow ("flow.txt")
  1) Copy the content of File "flow.txt"
  2) Goto Menu --> "Import" --> "Zwischenablage" 
  3) Paste the copied code
  4) Press button "Import"
  
* Use "Implementieren" ("Deploy") is the right upper corner to start the flow




Documentation:
* https://nodered.org/docs/getting-started/raspberrypi
* https://flows.nodered.org/node/node-red-dashboard
* https://flows.nodered.org/node/node-red-node-pi-neopixel
* https://flows.nodered.org/node/node-red-contrib-cpu
