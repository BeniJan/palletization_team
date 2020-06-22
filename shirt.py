class Shirt:
    def __init__(self, size, color):
        self.size = size.lower()
        self.color = color.lower()

    def __repr__(self):
        return str(self.size + "&" + self.color)