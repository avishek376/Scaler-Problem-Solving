class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        lst = []

        for i in range(B,C+1):
            lst.append(A[i])
        return lst

