class Rectangle:

    length = 0
    width = 0

    def __init__(self):
        self.width = 2
        self.length = 2

    def calc_area(self):
        return self.width * self.length

rect = Rectangle()
print(rect)
print(f"width: {rect.width}, length: {rect.length}")
print(f"area: {rect.calc_area()}")