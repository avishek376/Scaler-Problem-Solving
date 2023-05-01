class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in range(len(A)):
            res = res ^ A[i]

        return res

