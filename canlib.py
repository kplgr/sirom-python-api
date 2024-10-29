import can
from siromlib import SiromCommand

class CanBusTransport:
    def __init__(self, identifier:str):
        raise NotImplemented()
    

    def sendCommand(self, command: SiromCommand):
        raise NotImplemented()
    
    def shutdown(self):
        raise NotImplemented()




class LinuxCanBusTransport(CanBusTransport):
    def __init__(self, identifier:str):

        targetCan = f"/sys/class/net/{identifier}/flags"

        try:
            with open(targetCan, 'r') as file:
                data = file.read().replace('\n', '')
                
                if not list(data).pop() == '1':
                    raise Exception(f"Network adapter {identifier} is not configured")
                
        except:
            raise Exception(f"Network adapter {identifier} is not configured")

        self.__canBus = can.interface.Bus(channel = identifier, bustype = 'socketcan')

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.shutdown()

    def sendCommand(self, canbusTargetIdentifer:int, command: SiromCommand, timeoutSeconds:int = 2, verbose=False):
        canMessage = can.Message(arbitration_id=canbusTargetIdentifer, extended_id=False, data=command.toByteArray())
        self.__canBus.send(canMessage, timeoutSeconds)

        if verbose:
            print("Sent message:" )
            print(canMessage)


    def shutdown(self):
        self.__canBus.shutdown()
            

