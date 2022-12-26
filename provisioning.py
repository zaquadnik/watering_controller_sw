from json import *

class Settings:
    self.NumOfValves = 0
    self.PumpGpioNum = 0
    self.ValveConfigs = []
    def __init__(self, Path):
        try:
            JsonFile = open(Path)
        except:
            print("Error: Configuration file not found")
        else:
            Configuration = json.load(JsonFile)
            try:
                self.NumOfValves = Configuration['settings']['NumOfValves']
                self.PumpGpioNum = Configuration['settings']['PumpGpioNum']
                self.ValveConfigs = Configuration['ValveConfigs']
                if len(self.ValveConfigs) != self.NumOfValves:
                    raise KeyError("Invalid NumOfValves")
            except KeyError:
                print("Malformed configuration JSON") 
        finally:
            JsonFile.close()
            
    def GetValveConfig(self, ValveIndex):
        if ValveIndex >= self.NumOfValves:
            print("It's not valve you're looking for.")
        else:
            ValveCfg = self.ValveConfigs[ValveIndex]
            return[ValveCfg['GpioNum'], ValveCfg['PlanPath']]

class Workplan:
    self.Workplan = []
    def __init__(self, Path):
        try:
            WorkplanFile = open(Path)
        except:
            print("Error: Workplan file not found")
        else:
            WorkplanCfg = json.load(WorkplanFile)
        finally:
            WorkplanFile.close()
        