
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A % 9 == 1:
            return 1
        return 0

'''
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def sum_digits(number):
            if number == 0:
                return 0
            t = number % 10
            return t + sum_digits(number // 10)

        A = sum_digits(A)
        if A % 10 and (A // 10 == 0):
            return 1 if A == 1 else 0
        return self.solve(A)
'''





