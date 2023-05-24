class ComplexNumber:
    real = 0.0
    imaginary = 0.0

    # Define constructor here
    def __init__(self, x, y):
        self.real = x
        self.imaginary = y

    def add(self, x: "ComplexNumber") -> "ComplexNumber":
        # Complete the function
        a = complex(self.real, self.imaginary)
        b = complex(x.real, x.imaginary)
        s = a + b
        return ComplexNumber(s.real, s.imag)

    def subtract(self, x: "ComplexNumber") -> "ComplexNumber":
        # Complete the function
        a = complex(self.real, self.imaginary)
        b = complex(x.real, x.imaginary)
        s = a - b
        return ComplexNumber(s.real, s.imag)

    def multiply(self, x: "ComplexNumber") -> "ComplexNumber":
        # Complete the function
        a = complex(self.real, self.imaginary)
        b = complex(x.real, x.imaginary)
        s = a * b
        return ComplexNumber(s.real, s.imag)

    def divide(self, x: "ComplexNumber") -> "ComplexNumber":
        # Complete the function
        a = complex(self.real, self.imaginary)
        b = complex(x.real, x.imaginary)
        s = a / b
        return ComplexNumber(s.real, s.imag)

# a = ComplexNumber(10, 5)
# b = ComplexNumber(2, 3)
# c1 = a.add(b)
# c2 = a.subtract(b)
# c3 = a.multiply(b)
# c4 = a.divide(b)