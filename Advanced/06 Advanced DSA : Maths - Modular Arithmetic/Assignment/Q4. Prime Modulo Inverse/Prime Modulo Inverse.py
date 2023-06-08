import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        def power(a, b, p):
            if b == 0:
                return 1

            if b % 2 == 0:
                return power((a * a) % p, b // 2, p)
            else:
                return a * power((a * a) % p, (b - 1) // 2, p) % p

        # using Fermat's little theorem
        f = power(A, B - 2, B) % B
        return f


'''
def power(x, y, p): 
    res = 1        # Initialize result 
    x = x % p      # Update x if it is more than or equal to p 
    while (y > 0): 
        # If y is odd, multiply x with result 
        if (y & 1): 
            res = (res * x) % p 
        y = y >> 1 
        x = (x * x) % p
    return res

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Modular inverse of A Modulo B = pow(A, B - 2, B)
        return power(A, B - 2, B)
'''