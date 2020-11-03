
class Rectangle:
    """
    Super class
    """
    def __init__(self, base, height):
        """
        initialice the class
        """
        self.base = base
        self.height = height

    def find_area(self):
        return self.base * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

if __name__ == "__main__":
    my_rectangle = Rectangle(7, 5)
    
    print(my_rectangle.find_area())
    
    my_square = Square(7)
    
    print(my_square.find_area())
