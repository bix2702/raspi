#!/usr/bin/python 
from gpiozero import CPUTemperature
from rpi_ws281x import *
from time import sleep

# setup pin and number of LEDs
TOTAL_LED_COUNT = 5
LED_PIN = 18

# setup NeoPixel Leds (Alternative: Adafruit_NeoPixel( ...) )
strip = PixelStrip(TOTAL_LED_COUNT, LED_PIN)

# readout of ‘/sys/class/thermal/thermal_zone0/temp’
cpu = CPUTemperature()

# start invinite loop
while True:
	temp = cpu.temperature
	print(‘CPU temp: {}°C’.format(temp))
	
	strip.begin()
	for led in range(5):
		strip.setPixelColor(led, Color(0, 0, 0))

	if temp > 40.0:
		strip.setPixelColor(0, Color(0, 255, 0))
	if temp > 50.0:
		strip.setPixelColor(1, Color(255, 255, 0))
	if temp > 60.0:
		strip.setPixelColor(2, Color(255, 128, 0))
	if temp > 70.0:
		strip.setPixelColor(3, Color(255, 0, 255))
	if temp > 80.0:
		strip.setPixelColor(4, Color(255, 0, 0))
	
	strip.show()
	sleep(0.2)	
