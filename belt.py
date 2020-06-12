class Belt:

    def __init__(self, arduinoBoard):
        self.board = arduinoBoard
        self.time = __import__('time')

    def rollBelt(self, shirtUnits):
        print("Moving belt forward to " + str(shirtUnits) + " shirt unit.")
        # self.board.analog[{PORTA_DO_SERVO_DA_ESTEIRA}].write(120)
        # self.time.sleep(1.5)
        # self.board.analog[{PORTA_DO_SERVO_DA_ESTEIRA}].write(0)