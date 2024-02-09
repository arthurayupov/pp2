class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length


square_shape = Square(5)
print("Area of the square:", square_shape.area())
generic_shape = Shape()
print("Area of the generic shape:", generic_shape.area())
