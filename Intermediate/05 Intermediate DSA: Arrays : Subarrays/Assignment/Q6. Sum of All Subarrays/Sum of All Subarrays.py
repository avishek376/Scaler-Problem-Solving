class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):
        n = len(A)

        res = 0
        for i in range(n):
            summ = 0
            summ += (i + 1) * (n - i)
            res += A[i] * summ
        return res
