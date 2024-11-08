from time import *
from valvectrl import *
from pumpctrl import *
from provisioning import *

#Init valve control
# GPIOs for valve control:
#   23, 24, 25, 27

Settings = Settings("settings/settings.json")

WaterPump = Pump(Settings.GetPumpGpio())
WaterPump.ChangeState(pState.STOPPED)

for ValveIndex in range(Settings.NumOfValves):
    Valve[ValveIndex] = Valve(Settings.GetValveName(ValveIndex), Settings.GetValveGpio(ValveIndex))
    Workplans[ValveIndex] = Workplan(Settings.GetValveWorkplanPath(ValveIndex))
    Valve[ValveIndex].UpdateWorkPlan(Workplans[ValveIndex].GetWorkplan())


while True:
    sleep(1)
    ActiveValves = 0
    for ValveIndex in range(Settings.NumOfValves):
        Valve[ValveIndex].CheckTimeAndUpdate()
        if Valve[ValveIndex].GetState() == vState.OPENED:
            ActiveValves += 1
    if ActiveValves > 0:
        WaterPump.ChangeState(pState.WORKING)
    else:
        WaterPump.ChangeState(pState.STOPPED)
 