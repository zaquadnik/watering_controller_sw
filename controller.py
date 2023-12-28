import json
from time import *
from valvectrl import *

#Init valve control
# GPIOs for valve control:
#   23, 24, 25, 27

try:
    CfgFile = open("settings/settings.json","r")
    Config = json.load(CfgFile)
except:
    print("No config file found")
finally:
    CfgFile.close()



RinserValve = Valve('Rinsers', 23)
WateringValve = Valve('Watering', 24)

ExampleWorkPlan = [[[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]],   #Monday
                   [[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]],   #Tuesday
                   [[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]],   #Wednesday
                   [[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]],   #Thursday
                   [[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]],   #Friday
                   [[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]],   #Saturday
                   [[time(10,00,00),time(10,15,00)],[time(19,00,00),time(19,15,00)]]]   #Sunday

RinserValve.UpdateWorkPlan(ExampleWorkPlan)
WateringValve.UpdateWorkPlan(ExampleWorkPlan)


while True:
    sleep(1)
    RinserValve.CheckTimeAndUpdate()
    WateringValve.CheckTimeAndUpdate()


