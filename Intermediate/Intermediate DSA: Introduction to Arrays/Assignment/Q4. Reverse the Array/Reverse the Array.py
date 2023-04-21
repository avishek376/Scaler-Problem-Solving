class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        lst = []
        for i in range(len(A)-1, -1, -1):
            lst.append(A[i])
        return lst



