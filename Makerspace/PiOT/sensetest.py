#sensetest.py
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

for i in range(5):
	pressure = sense.get_pressure()
	print(pressure)
	sleep(1)