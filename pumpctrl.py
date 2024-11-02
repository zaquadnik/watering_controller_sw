from relay import *
from enum import Enum

class pState(Enum):
    STOPPED = 0
    WORKING = 1

class Pump:
    def __init__(self, GpioNum):
        self.PumpGpio = GpioNum
        self.State = pState.STOPPED
        self.PumpRelay = Relay(GpioNum)
        self.PumpRelay.TurnOff()

    def ChangeState(self, State):
        self.State = State
        match(State):
            case pState.STOPPED:
                self.PumpRelay.TurnOff()
            case pState.WORKING:
                self.PumpRelay.TurnOn()
            case _:
                raise ValueError("Not correct pump state.")