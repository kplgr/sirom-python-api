from siromlib import SiromCommand, SiromCommandType, SiromMotorSpeed, SiromPowerConfig
from canlib import LinuxCanBusTransport
import time


cmdPowerOn = SiromCommand(SiromCommandType.POWER_ON, SiromMotorSpeed(50), SiromPowerConfig.POWERCFG_F2R)
cmdOperate = SiromCommand(SiromCommandType.GOTO_OPER, SiromMotorSpeed(50), SiromPowerConfig.POWERCFG_F2R)

cmdLatch = SiromCommand(SiromCommandType.GOTO_LAT, SiromMotorSpeed(50), SiromPowerConfig.POWERCFG_F2R)
cmdRelease = SiromCommand(SiromCommandType.GOTO_RTC, SiromMotorSpeed(50), SiromPowerConfig.POWERCFG_F2R)
cmdStop = SiromCommand(SiromCommandType.STOP)



with LinuxCanBusTransport('can0') as bus:

    commands = [cmdPowerOn, cmdOperate, cmdLatch, cmdStop, cmdRelease, cmdStop]

    siromId = 0x01

    for idc, command in enumerate(commands):

        print(f"Sending bus command {idc+1}")
        bus.sendCommand(siromId, command)

        if command.type == SiromCommandType.GOTO_LAT or command.type == SiromCommandType.GOTO_RTC:
            time.sleep(6)
        
        time.sleep(2)