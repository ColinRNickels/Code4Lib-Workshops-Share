#sensethree.py

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

for i in range(5):
	pressure = sense.get_pressure()
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
	print(pressure)
	print(temp)
	print(humidity)
	print("#" * 72)
	sleep(1)