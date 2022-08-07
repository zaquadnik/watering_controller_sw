from time import *
from relay import *

FirstValve = Relay(23)
SecondValve = Relay(24)

while True:
    FirstValve.TurnOn()
    sleep(1)
    SecondValve.TurnOn()
    sleep(1)
    FirstValve.TurnOff()
    sleep(1)
    SecondValve.TurnOff()
    sleep(1)

