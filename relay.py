from RPi.GPIO import *

class Relay:
    def __init__(self, GpioNum):
        self.GpioNum = GpioNum
        setmode(BCM)
        setup(GpioNum, OUT)

    def TurnOn(self):
        output(self.GpioNum, HIGH)

    def TurnOff(self):
        output(self.GpioNum, LOW)
