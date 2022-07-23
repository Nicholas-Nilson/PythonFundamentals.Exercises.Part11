class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

