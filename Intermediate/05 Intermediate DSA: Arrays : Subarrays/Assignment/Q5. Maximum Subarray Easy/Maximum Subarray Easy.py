class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):

        result = 0
        n = A
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += C[j]
                if summ <= B:
                    result = max(result, summ)

        return result