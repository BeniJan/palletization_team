from math import ceil
from box import Box
from shirt import Shirt

class Palletizer:
    def __init__(self, disorderedShirtList):
        self.copy = __import__("copy")

        self.shirtList = disorderedShirtList
        self.dynamicShirtList = self.copy.deepcopy(self.shirtList)
        
        self.models = {
            "big&blue": [],
            "big&yellow": [],
            "big&red": [],
            "small&blue": [],
            "small&yellow": [],
            "small&red": [],
        }

        self.boxes = []

        self.trapdoorLabels = [
            "big&blue",
            "big&yellow",
            "big&red",
            "small&blue",
            "small&yellow",
            "small&red"
        ]

        self.droppedShirtsCounters = {
            "big": 0,
            "small": 0
        }

        self.currentBox = {
            "big": Box("big"),
            "small": Box("small")
        }

    def separateByModel(self):
        for i, shirt in enumerate(self.shirtList):
            currentModel = repr(shirt)

            self.models[currentModel].append(i)

        return self.models

    def getTrapdoorsOrder(self):

        trapdoorsOrder = []

        for i, shirt in enumerate(self.shirtList):
            
            trapdoorModels = []
            
            for model in self.trapdoorLabels:
                trapdoorModels.append(model)

            try:
                destiny = self.trapdoorLabels.index(str(shirt)) + 1

                iterator = 1
                shirtAllocated = False

                while not shirtAllocated:
                    if trapdoorsOrder.count(self.trapdoorLabels.index(str(shirt)) + iterator) < 10:
                        destiny = self.trapdoorLabels.index(str(shirt)) + iterator
                        shirtAllocated = True
                    else:
                        iterator += 1

            except:
                for i, label in enumerate(self.trapdoorLabels):
                    if str(shirt) in label and len(label):
                        destiny = i + 1

            trapdoorsOrder.append(destiny)

        return trapdoorsOrder

    def countSizeDrop(self, shirtIndex):
        shirtModel = repr(self.shirtList[shirtIndex])
        size = self.extractSize(shirtModel)
        self.droppedShirtsCounters[size] += 1
        self.currentBox[size].addShirt(self.extractColor(shirtModel))
        print("\nA " + repr(self.shirtList[shirtIndex]) + " shirt have been placed\n")
        self.dynamicShirtList.pop(0)
        return size

    def extractSize(self, reprString):
        return reprString.split("&")[0]

    def extractColor(self, reprString):
        return reprString.split("&")[1]

    def getPlacedShirtsCounter(self, size):
        return self.droppedShirtsCounters[size]

    def clearCounter(self, sizeToBeCleaned):
        self.droppedShirtsCounters[sizeToBeCleaned] = 0

    def clearCounters(self):
        self.droppedShirtsCounters["big"] = 0
        self.droppedShirtsCounters["small"] = 0
    
    def cleanAttributes(self):
        self.models = {
            "big&blue": [],
            "big&yellow": [],
            "big&red": [],
            "small&blue": [],
            "small&yellow": [],
            "small&red": [],
        }