import RPI.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.output(12, True)
gpio.output(12, False)