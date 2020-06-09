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

shirtDisorderedList = [ # Will be injected by I2C in a near future
    Shirt("big", "yellow"),
    Shirt("small", "yellow"),
    Shirt("small", "yellow"),
    Shirt("small", "blue"),
    Shirt("small", "blue"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "red"),
    Shirt("small", "red"),
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
    Shirt("big", "yellow"),
    Shirt("big", "yellow"),
    Shirt("big", "blue"),
    Shirt("big", "blue"),
    Shirt("big", "yellow")
]

palletizer = Palletizer(shirtDisorderedList)
shirtsDestiny = []
currentSize = ""



while palletizer.dynamicShirtList:
    if not controller.shirtInBelt():
        continue

    palletizer.shirtList
    palletizer.dynamicShirtList
    palletizer.separateByModel()
    palletizer.labelTrapdoors()

    shirtsDestinys = palletizer.getTrapdoorsOrder()
    for i, destiny in enumerate(shirtsDestinys):
        controller.moveShirt(destiny)
        currentSize = palletizer.countSizeDrop(i)

        if 10 in palletizer.droppedShirtsCounters.values():

            for i, trapdoor in enumerate(palletizer.trapdoorLabels):
                if palletizer.extractSize(trapdoor) == currentSize:

                    while not controller.boxUnderRamp():
                        continue

                    controller.trapdoors.drop(i + 1)
                    controller.trapdoors.close(i + 1)

            print("\n\n Current box is ready, loaded with " + str(palletizer.getPlacedShirtsCounter(currentSize)) + " shirts\n\n")

            while False: # controller.boxUnderRamp():
                continue

            palletizer.clearCounter(currentSize)

    if palletizer.getPlacedShirtsCounter("big") > 0:
        for i, trapdoor in enumerate(palletizer.trapdoorLabels):
            if palletizer.extractSize(trapdoor) == "big":

                while not controller.boxUnderRamp():
                    continue

                controller.trapdoors.drop(i + 1)
                controller.trapdoors.close(i + 1)

            while False: # controller.boxUnderRamp():
                continue

        print("\n\n Current box is ready, loaded with " + str(palletizer.getPlacedShirtsCounter("big")) + " shirts\n\n")

    if palletizer.getPlacedShirtsCounter("small") > 0:
        for i, trapdoor in enumerate(palletizer.trapdoorLabels):
            if palletizer.extractSize(trapdoor) == "small":

                while not controller.boxUnderRamp():
                    continue

                controller.trapdoors.drop(i + 1)
                controller.trapdoors.close(i + 1)

            while False: # controller.boxUnderRamp():
                continue

        print("\n\n Current box is ready, loaded with " + str(palletizer.getPlacedShirtsCounter("small")) + " shirts\n\n")

    palletizer.cleanAttributes()
    palletizer.clearCounters()

print("its over")