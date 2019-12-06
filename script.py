#!/usr/bin/python 
from gpiozero import CPUTemperature
from rpi_ws281x import *
from time import sleep

# Init LED stripe
TOTAL_LED_COUNT = 5
LED_PIN = 18
strip = Adafruit_NeoPixel(TOTAL_LED_COUNT, LED_PIN)

# readout of ‘/sys/class/thermal/thermal_zone0/temp’
cpu = CPUTemperature()

while True:
	temp = cpu.temperature
	print(‘CPU temp: {}°C’.format(temp))
	strip.begin()
	if temp > 40.0:
		strip.setPixelColorRGB(0, 0, 255, 0)
	if temp > 50.0:
		strip.setPixelColorRGB(1, 0, 128, 128)
	if temp > 60.0:
		strip.setPixelColorRGB(2, 0, 255, 255)
	if temp > 70.0:
		strip.setPixelColorRGB(3, 128, 255, 0)
	if temp > 80.0:
		strip.setPixelColorRGB(4, 255, 0, 0)
	strip.show()
	sleep(0.2)	
