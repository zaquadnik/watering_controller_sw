import json
from time import *
from valvectrl import *
from pumpctrl import *
from provisioning import *

#Init valve control
# GPIOs for valve control:
#   23, 24, 25, 27

<<<<<<< HEAD
try:
    CfgFile = open("settings/settings.json","r")
    Config = json.load(CfgFile)
except:
    print("No config file found")
finally:
    CfgFile.close()



RinserValve = Valve('Rinsers', 23)
WateringValve = Valve('Watering', 24)
=======
Settings = Settings("settings/settings.json")
>>>>>>> bfdb964f6a095635c25b7f5701d86962325f7d42

WaterPump = Pump(Settings.GetPumpGpio())
WaterPump.ChangeState(STOPPED)

for ValveIndex in range(Settings.NumOfValves):
    Valve[ValveIndex] = Valve(Settings.GetValveName(ValveIndex), Settings.GetValveGpio(ValveIndex))
    Workplans[ValveIndex] = Workplan(Settings.GetValveWorkplanPath(ValveIndex))
    Valve[ValveIndex].UpdateWorkPlan(Workplans[ValveIndex].GetWorkplan())


while True:
    sleep(1)
    ActiveValves = 0
    for ValveIndex in range(Settings.NumOfValves):
        Valve[ValveIndex].CheckTimeAndUpdate()
        if Valve[ValveIndex].GetState() == OPENED:
            ActiveValves += 1
    if ActiveValves > 0:
        WaterPump.ChangeState(WORKING)
    else:
        WaterPump.ChangeState(STOPPED)
 