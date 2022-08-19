from relay import *

STOPPED = 0
WORKING = 1

class Pump:
    def __init__(self, GpioNum):
        self.PumpGpio = GpioNum
        self.State = STOPPED
        self.PumpRelay = Relay(GpioNum)
        self.PumpRelay.TurnOff()

    def ChangeState(self, State):
        self.State = State
        match(State):
            case STOPPED:
                self.PumpRelay.TurnOff()
            case WORKING:
                self.PumpRelay.TurnOn()
            case _:
                raise ValueError("Not correct pump state.")