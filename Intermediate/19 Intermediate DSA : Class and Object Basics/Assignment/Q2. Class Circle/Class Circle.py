class Circle:
    # Define properties here
    pi = 3.14
    r = 0

    # Define constructor here
    def __init__(self, a):
        self.r = a

    def perimeter(self):
        # Complete the function
        return 2 * self.pi * self.r

    def area(self):
        # Complete the function
        return self.pi * (self.r) ** 2

# a = new Circle(3)  // Radius = 3
# a.perimeter() // 18.84
# a.area() // 28.26