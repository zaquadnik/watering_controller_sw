from time import *
from valvectrl import *

#Init valve control
# GPIOs for valve control:
#   23, 24, 25, 27

RinserValve = Valve('Rinsers', 23)

while True:
    sleep(1)


