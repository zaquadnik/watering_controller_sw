from time import *
from valvectrl import *
from provisioning import *

#Init valve control
# GPIOs for valve control:
#   23, 24, 25, 27

Settings = Settings("settings/settings.json")

for ValveIndex in range(Settings.NumOfValves):
    Valve[ValveIndex] = Valve(Settings.GetValveName(ValveIndex), Settings.GetValveGpio(ValveIndex))
    Workplans[ValveIndex] = Workplan(Settings.GetValveWorkplanPath(ValveIndex))
    Valve[ValveIndex].UpdateWorkPlan(Workplans[ValveIndex].GetWorkplan())

#Add pump control & settings

while True:
    sleep(1)
    for ValveIndex in range(Settings.NumOfValves):
        Valve[ValveIndex].CheckTimeAndUpdate()
 