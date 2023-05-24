def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


class Fraction:
    # Define constructor here

    def __init__(self, u, v):
        self.numerator = u
        self.denominator = v

    def add(self, a):
        # Complete the function

        denom = self.denominator * a.denominator
        num = self.denominator * a.numerator + self.numerator * a.denominator
        temp = gcd(abs(num), abs(denom))

        num //= temp
        denom //= temp
        return Fraction(num, denom)

    def subtract(self, a):
        # Complete the function

        denom = self.denominator * a.denominator;
        num = self.numerator * a.denominator - self.denominator * a.numerator;
        temp = gcd(abs(num), abs(denom))

        num //= temp
        denom //= temp
        return Fraction(num, denom)

    def multiply(self, a):
        # Complete the function

        denom = self.denominator * a.denominator
        num = self.numerator * a.numerator
        temp = gcd(abs(num), abs(denom))

        num //= temp
        denom //= temp
        return Fraction(num, denom)

# x = Fraction(2, 3)  // 2/3
# y = Fraction(4, 5) // 4/5
# z = x.add(y) // 22/15
# z = x.subtract(y) // -2/15
# z = x.multiply(y) // 8/15
