import Rpi.GPIO as GPIO
import time

class led:
	def __init__(self, portnummer):
		self.portNummer = portNummer
		GPIO.sertwarnings(False)
		Gpio.setmode(GPIO.BCM)
		GPIO.setup(portNummer, GPIO.OUT)

	def on(self):
		GPIO.output(self.portNummer, 1)
	def off(self):
		GPIO.output(self.portNummer, 0)

led1 = led(24)
led2 = led(25)

led1.on
time.sleep(1)
led1.off
led2.on
time.sleep(1)
led2.off
led1.on
