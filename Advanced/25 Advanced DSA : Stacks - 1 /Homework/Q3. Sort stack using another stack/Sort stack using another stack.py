class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        B = []
        while A:
            x = A.pop()
            while B and B[-1] > x:
                y = B.pop()
                A.append(y)
            B.append(x)
        return B
