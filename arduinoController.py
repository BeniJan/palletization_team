try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install', 'pyfirmata'])
    from pyfirmata import Arduino, util

from belt import Belt
from mechanicalClaw import MechanicalClaw
from trapdoors import Trapdoors

class ArduinoController:

    def __init__(self, board, clawObj, beltObj, trapdoorObj):
        self.board = board

        self.claw = clawObj
        self.belt = beltObj
        self.trapdoors = trapdoorObj

        self.time = __import__('time')

    def setup(self):
        self.claw.reset()
        self.trapdoors.closeAll()

    def shirtInBelt(self):
        # return self.board.digital[{PORTA_DO_INFRAVERMELHO_DA_ESTEIRA}].read()
        return True

    def boxUnderRamp(self):
        # return self.board.digital[{PORTA_DO_INFRAVERMELHO_DA_CAIXA}].read()
        return True
    
    def moveShirt(self, destinyTrapdoor):
        self.claw.reset()
        self.belt.rollBelt(1)
        self.claw.grab()
        self.claw.move(destinyTrapdoor)
        self.claw.drop()

    def openTrapdoor(self, trapdoor):
        self.trapdoors.drop(trapdoor)

    def closeTrapdoor(self, trapdoor):
        self.trapdoors.close(trapdoor)
    
    def closeAllTrapdoors(self):
        self.trapdoors.closeAll()

    def pingTest(self):
        for i in range(5):
            self.board.digital[13].write(1)
            print("aceso")
            self.time.sleep(1)
            self.board.digital[13].write(0)
            print("apagado")
            self.time.sleep(1)