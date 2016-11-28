#! /usr/bin/python3

# Set RPI pin numbers
#portIn1 = 24
#portOut1 = 25


#import part
import RPi.GPIO as GPIO
from time import sleep
import time,os,pickle,threading

class HardwareInter(threading.Thread):
	def __init__(self):
		super(HardwareInterface, self).__init__()
		self.setDaemon(True)
		self.running = False
		# Set RPI pin numbers
		self.portIn1 = 24
		self.portOut1 = 25
		GPIO.setwarnings(False)
		# Set GPIO pins
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.portOut1, GPIO.OUT)
		GPIO.setup(self.portIn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

		# Setup internal state
		os.chdir('/home/pi/Documents/Degu/Data')
		trail = 0
		time0 = time.time()
		time1 = time.time()
		time2 = time.time()
		jiKoku = []
		day = time.strftime("%Y-%m-%d")

		def timeRecord ():


		def trailRecord ():
