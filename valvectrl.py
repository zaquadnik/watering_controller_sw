from relay import *
from datetime import *

OPENED = 1
CLOSED = 0

#----------------------------------------------------------------------------
# WorkPlan is arranged as list indexed by the day of week. Each day contains
# multiple two-element lists, each containing on time and off time. Example:
#   WorkPlan[0] - contains day plan wor Monday
#   WorkPlan[0][0][0] - On time for first work period on Monday
#   WorkPlan[0][0][1] - Off time for first work period on Monday
# The time between on and off is working period.
#----------------------------------------------------------------------------

class Valve:
    def __init__(self, Name, GpioNum):
        self.name = Name
        self.ValveState = CLOSED
        self.CurrentTime = datetime.now()
        self.Programmed = False
        self.WorkPlan = []              #WorkPlan as list to contain planned ons and offs
        self.ValveGpio = Relay(GpioNum)
        self.ValveGpio.TurnOff()

    def UpdateTime(self):
        self.CurrentTime = datetime.now()

    def UpdateWorkPlan(self, WorkPlan):
        self.WorkPlan = WorkPlan
        self.Programmed = True

    def StateUpdate(self, ValveState):
        match ValveState:
            case CLOSED:
                self.ValveGpio.TurnOff()
                self.ValveState = ValveState
            case OPENED:
                self.ValveGpio.TurnOn()
                self.ValveState = ValveState
            case _:
                raise ValueError("Unable to change valve state.Not correct state value.")

    def CheckTimeAndUpdate(self):
        self.CurrentTime = datetime.now()
        if self.Programmed == True
            DayPlan = self.WorkPlan[self.CurrentTime.weekday()]
            LocalState = CLOSED
            # This loop checks whether current time is within one of working periods in day plan
            for i in DayPlan:
                if self.CurrentTime.time() >= DayPlan[i][0] and self.CurrentTime.time() < DayPlan[i][1]:
                    LocalState = OPENED
                    break
            self.StateUpdate(LocalState)





