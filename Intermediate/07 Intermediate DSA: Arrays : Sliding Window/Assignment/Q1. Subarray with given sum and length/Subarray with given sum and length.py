class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        summ = 0
        for i in range(B):
            summ += A[i]
        if summ == C:
            return 1

        start = 1
        end = B
        while end < n:
            summ = summ - A[start - 1] + A[end]
            if summ == C:
                return 1
            start += 1
            end += 1
        return 0
