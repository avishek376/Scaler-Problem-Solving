class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(len(A)):
            ans = ans ^ A[i]

        return ans

