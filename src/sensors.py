from signal import pause

from gpiozero import LineSensor

sensor = LineSensor(23)
sensor.when_line = lambda: print("line detected")
sensor.when_no_line = lambda: print("no line detected")
pause()
