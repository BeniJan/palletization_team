class Trapdoors:

    def __init__(self, arduinoBoard):
        self.board = arduinoBoard

        self.trapdoorsStates = dict([
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (6, False),
        ])

        self.time = __import__('time')

    def drop(self, trapdoor):
        if self.trapdoorsStates.get(trapdoor):
            print("ERROR: Trapdoor already opened")
        else:
            print("\nOpening trapdoor number " + str(trapdoor))
            # self.board.analog[PORTA_DO_SERVO_DO_ALCAPAO_X].write(120)
            self.trapdoorsStates[trapdoor] = True

    def close(self, trapdoor):
        if not self.trapdoorsStates.get(trapdoor):
            print("ERROR: Trapdoor already closed")
        else:
            print("Closing trapdoor number " + str(trapdoor) + "\n")
            # self.board.analog[{PORTA_DO_SERVO_DO_ALCAPAO_X}].write(30)
            self.trapdoorsStates[trapdoor] = False


    def dropAll(self):
        print("Opening all trapdoors")
        for i in self.trapdoorsStates:
            # self.board.analog[{PORTA_DO_SERVO_DO_ALCAPAO_i}].write(120)
            self.trapdoorsStates[i + 1] = True

    def closeAll(self):
        print("Closing all trapdoors")
        for i in self.trapdoorsStates:
            # self.board.analog[{PORTA_DO_SERVO_DO_ALCAPAO_i}].write(30)
            self.trapdoorsStates[i + 1] = False