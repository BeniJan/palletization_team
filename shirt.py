class Shirt:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __repr__(self):
        return str(self.size + "&" + self.color)