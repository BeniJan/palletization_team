try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install', 'pyfirmata'])
    from pyfirmata import Arduino, util

from time import sleep

from palletizer import Palletizer
from shirt import Shirt
from arduinoController import ArduinoController
from belt import Belt
from mechanicalClaw import MechanicalClaw
from trapdoors import Trapdoors

board = Arduino('/dev/ttyACM0')

belt = Belt(board)
claw = MechanicalClaw(board)
trapdoors = Trapdoors(board)

controller = ArduinoController(board, claw, belt, trapdoors)

# Erase the example and insert your shirt list
shirtDisorderedList = [
    Shirt("big", "blue"), # a BIG and BLUE shirt
    Shirt("small", "blue"), # a SMALL and BLUE shirt
    Shirt("big", "red"), # a BIG and RED shirt
    Shirt("small", "red"), # Notice that the constructor
    Shirt("big", "yellow"), # is built by two arguments
    Shirt("small", "yellow") # first the color, then the size
]

palletizer = Palletizer(shirtDisorderedList)
shirtsDestiny = []
currentSize = ""

while palletizer.dynamicShirtList: # While there is any shirt in the provided list that wasn't placed and processed
    palletizer.separateByModel()
    shirtsDestinys = palletizer.getTrapdoorsOrder()

    if not controller.shirtInBelt(): # Check if there is any shirt in the belt using an infra-red sensor
        continue # Will do nothing until it returns True

    controller.setup() # Setups Controller

    finalReport = "\n\nBoxes built:\n\n" # Initialize final report

    for i, destiny in enumerate(shirtsDestinys):

        while controller.emergencyButtonPressed(): # Check for an emergency
            continue # Will pause the proccess until the button with lock is released

        controller.moveShirt(destiny) # Places the shirt
        currentSize = palletizer.countSizeDrop(i) # Proccesses the shirt 

        if 10 in palletizer.droppedShirtsCounters.values(): # If there is a way to build a full box, builds it

            for i, trapdoor in enumerate(palletizer.trapdoorLabels):
                trapdoorSize = palletizer.extractSize(trapdoor)

                if trapdoorSize == currentSize:
                    while not controller.boxUnderRamp() or controller.emergencyButtonPressed(): # Security checkers
                        continue
                    controller.openTrapdoor(i + 1) # Release trapdoors that contains desired shirts

                    while controller.emergencyButtonPressed():  # Security checker
                        continue

                    controller.closeTrapdoor(i + 1) # Prepare them to receive next shirts

            print(palletizer.currentBox[trapdoorSize])
            finalReport +=  repr(palletizer.currentBox[trapdoorSize]) # Register released shirts in final report
            palletizer.currentBox[trapdoorSize].emptyBox() # Reinitialize boxes counters

            while False: # controller.boxUnderRamp():
                continue

            palletizer.clearCounter(currentSize)

    if palletizer.getPlacedShirtsCounter("big") > 0: # If there are any big shirts left, build a incomplete box

        for i, trapdoor in enumerate(palletizer.trapdoorLabels):
            if palletizer.extractSize(trapdoor) == "big":

                while not controller.boxUnderRamp() or controller.emergencyButtonPressed():
                    continue
                controller.openTrapdoor(i + 1)
                while controller.emergencyButtonPressed():
                    continue
                controller.closeTrapdoor(i + 1)

            while False: # controller.boxUnderRamp():
                continue

        print(palletizer.currentBox["big"])
        finalReport +=  repr(palletizer.currentBox[trapdoorSize])
        palletizer.currentBox["big"].emptyBox()

    if palletizer.getPlacedShirtsCounter("small") > 0: # If there are any big shirts left, build a incomplete box

        for i, trapdoor in enumerate(palletizer.trapdoorLabels):
            if palletizer.extractSize(trapdoor) == "small":
                while not controller.boxUnderRamp() or controller.emergencyButtonPressed():
                    continue
                controller.openTrapdoor(i + 1)
                while controller.emergencyButtonPressed():
                    continue
                controller.closeTrapdoor(i + 1)

            while False: # controller.boxUnderRamp():
                continue

        print(palletizer.currentBox["small"])
        finalReport +=  repr(palletizer.currentBox[trapdoorSize])
        palletizer.currentBox["small"].emptyBox()

    palletizer.cleanAttributes() # Prepare for next round
    palletizer.clearCounters()

    print(finalReport) # Plot the report :)