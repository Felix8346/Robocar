from gpiozero import LineSensor
from signal import pause
sensor = LineSensor (23)
sensor.when_line = lambda: print ("line detected")
sensor.when_no_line = lambda: print("no line detected")
pause ()





