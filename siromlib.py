from enum import Enum


class SiromCommandType(Enum):
    STOP = 0x00
    GOTO_RTC = 0x01
    GOTO_LAT = 0x02
    GOTO_STB = 0x03
    GOTO_OPER = 0x04
    POWER_ON = 0x05
    POWER_OFF = 0x06


class SiromPowerConfig(Enum):
	POWERCFG_OFF = 0x00
	POWERCFG_F2R = 0x01
	POWERCFG_R2F = 0x02
	POWERCFG_BID = 0x03

class SiromMotorSpeed():
    def __init__(self, speedPercentage:int = 50):
          
        if not (speedPercentage < 100 and speedPercentage > 0):
            speedPercentage = 50

        self.__speedPercentage = speedPercentage

    @property
    def speedPercentage(self):
        return self.__speedPercentage
          

class SiromCommand():
    def __init__(self, 
        commandType: SiromCommandType, 
        motorSpeed:SiromMotorSpeed = SiromMotorSpeed(50), 
        powerConfig: SiromPowerConfig = SiromPowerConfig.POWERCFG_F2R
    ):
        self.__commandType = commandType
        self.__motorSpeed = motorSpeed
        self.__powerConfig = powerConfig

    def toByteArray(self, numberOfBytes = 8):
        actualMessageBytes = [ 0x01, self.__commandType.value, self.__motorSpeed.speedPercentage, self.__powerConfig.value ]

        paddedMessageBytes = actualMessageBytes
        
        while len(paddedMessageBytes) < numberOfBytes:
            paddedMessageBytes.append(0)

        
        return paddedMessageBytes
        
    @property
    def type(self):
        return self.__commandType


if __name__ == '__main__':
    pass


    

