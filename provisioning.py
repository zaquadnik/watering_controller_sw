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
            return[ValveCfg['GpioNum'], ValveCfg['PlanPath'], ValveCfg['Name']]
        
    def GetValveGpio(self, ValveIndex):
        return self.GetValveConfig(ValveIndex)[0]
    
    def GetValveWorkplanPath(self, ValveIndex):
        return self.GetValveConfig(ValveIndex)[1]
    
    def GetValveName(self, ValveIndex):
        return self.GetValveConfig(ValveIndex)[2]
    
    def GetPumpGpio(self):
        return self.PumpGpioNum
        
class Workplan:
    self.Workplan = []
    self.DaysOfWeek = {'mon' : 0, 'tue' : 1, 'wed' : 2, 'thu': 3, 'fri' : 4, 'sat' : 5, 'sun' : 6}
    self.WorkplanFilePath = ''
    def __init__(self, Path):
        self.WorkplanFilePath = Path
        self.ReloadWorkPlan()
        
    def GetWorkplan(self):
        return self.WorkPlan
    
    def ReloadWorkplan(self):
        try:
            WorkplanFile = open(self.WorkplanFilePath)
        except:
            self.WorkplanFilePath = ''
            print("Error: Workplan file not found or invalid file path")
        else:
            WorkplanCfg = json.load(WorkplanFile)
            for Day in WorkplanCfg['day']:
                i = self.DaysOfWeek[WorkplanCfg['day'][Day]]
                DayPlan = list(WorkplanCfg['day'][Day].values())
                for State in DayPlan:
                    for Time in DayPlan[State]:
                        WorkPlan[i][Time][State] = datetime.strptime(DayPlan[State][Time], '%H:%M').time()
        finally:
            WorkplanFile.close()
        
        