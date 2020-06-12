class MechanicalClaw:

    def __init__(self, arduinoBoard):
        self.board = arduinoBoard

        self.position = 0
        self.isOpen = True
        self.time = __import__('time')

    def move(self, destinyPosition):
        if self.position == destinyPosition:
            print("Mechanical claw already at position " + str(self.position))
        else:
            print("Moving the mechanical claw from position number " + str(self.position) + " to number " + str(destinyPosition))
            # self.board.analog[{PORTA_DO_SERVO_DO_TRILHO_DA_GARRA_MECANICA}].write({POSICAO_DO_ALCAPAO_NUMERO_destinyPosition})
            self.position = destinyPosition

    def grab(self):
        print("Closing the mechanical claw")
        # self.board.digital[{PORTA_DO_SERVO_DA_GARRA_MECANICA}].write(1)
        self.isOpen = False

    def drop(self):
        print("Opening the mechanical claw")
        # self.board.digital[{PORTA_DO_SERVO_DA_GARRA_MECANICA}].write(0)
        self.isOpen = True

    def reset(self):
        print("Reseting mechanical claw")
        self.move(0)
        self.drop()