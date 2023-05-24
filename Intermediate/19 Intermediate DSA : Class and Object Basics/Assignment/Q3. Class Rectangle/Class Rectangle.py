class Rectangle:
    # Define properties here
    l = 0
    b = 0

    # Define constructor here
    def __init__(self, Length, Breadth):
        self.l = Length
        self.b = Breadth

    def perimeter(self):
        # Complete the function
        return 2 * (self.l + self.b)

    def area(self):
        # Complete the function
        return (self.l * self.b)

# a = Rectangle(2, 3)  // Length = 2, Breadth = 3
# a.perimeter() // Should give 10
# a.area() // Should give 6