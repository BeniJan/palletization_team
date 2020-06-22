class Box:

    def __init__(self, size):
        self.size = size
        self.content = {}

    def addShirt(self, color):
        try:
            self.content[color] += 1
        except:
            self.content[color] = 1

    def emptyBox(self):
        self.content = {}

    def __repr__(self):
        representation = "{0} box have been built, containing {1} shirts:\n\n".format(self.size.capitalize(), sum(self.content.values()))
        for color, shirts in self.content.items():
            representation += "{0}: {1}\n".format(color.capitalize(), shirts)
        representation += "\n"

        return representation