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

shirtDisorderedList = [
    Shirt("big", "yellow"),
    Shirt("small", "yellow"),
    Shirt("small", "blue"),
    Shirt("small", "red"),
    Shirt("small", "yellow"),
    Shirt("small", "red"),
    Shirt("small", "blue"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "blue"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("big", "yellow"),
    Shirt("big", "yellow"),
    Shirt("big", "yellow"),
    Shirt("big", "blue"),
    Shirt("small", "blue"),
    Shirt("big", "yellow"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("big", "yellow"),
    Shirt("big", "blue"),
    Shirt("big", "yellow")
]

palletizer = Palletizer(shirtDisorderedList)
shirtsDestiny = []
currentSize = ""

while palletizer.dynamicShirtList:
    if not controller.shirtInBelt():
        continue

    palletizer.separateByModel()
    shirtsDestinys = palletizer.getTrapdoorsOrder()

    controller.setup()
    finalReport = "\n\nBoxes built:\n\n"
    for i, destiny in enumerate(shirtsDestinys):
        controller.moveShirt(destiny)
        currentSize = palletizer.countSizeDrop(i)

        if 10 in palletizer.droppedShirtsCounters.values():

            for i, trapdoor in enumerate(palletizer.trapdoorLabels):
                trapdoorSize = palletizer.extractSize(trapdoor)
                if trapdoorSize == currentSize:

                    while not controller.boxUnderRamp():
                        continue

                    controller.openTrapdoor(i + 1)
                    controller.closeTrapdoor(i + 1)

            print(palletizer.currentBox[trapdoorSize])
            finalReport +=  repr(palletizer.currentBox[trapdoorSize])
            palletizer.currentBox[trapdoorSize].emptyBox()

            while False: # controller.boxUnderRamp():
                continue

            palletizer.clearCounter(currentSize)

    if palletizer.getPlacedShirtsCounter("big") > 0:
        for i, trapdoor in enumerate(palletizer.trapdoorLabels):
            if palletizer.extractSize(trapdoor) == "big":

                while not controller.boxUnderRamp():
                    continue

                controller.openTrapdoor(i + 1)
                controller.closeTrapdoor(i + 1)

            while False: # controller.boxUnderRamp():
                continue

        print(palletizer.currentBox["big"])
        finalReport +=  repr(palletizer.currentBox[trapdoorSize])
        palletizer.currentBox["big"].emptyBox()

    if palletizer.getPlacedShirtsCounter("small") > 0:
        for i, trapdoor in enumerate(palletizer.trapdoorLabels):
            if palletizer.extractSize(trapdoor) == "small":

                while not controller.boxUnderRamp():
                    continue

                controller.openTrapdoor(i + 1)
                controller.closeTrapdoor(i + 1)

            while False: # controller.boxUnderRamp():
                continue

        print(palletizer.currentBox["small"])
        finalReport +=  repr(palletizer.currentBox[trapdoorSize])
        palletizer.currentBox["small"].emptyBox()

    palletizer.cleanAttributes()
    palletizer.clearCounters()

    print(finalReport)