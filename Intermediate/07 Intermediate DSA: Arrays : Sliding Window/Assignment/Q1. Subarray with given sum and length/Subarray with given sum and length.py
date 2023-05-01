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

        s = 1
        e = B
        while e < n:
            summ = summ - A[s - 1] + A[e]
            if summ == C:
                return 1
            s += 1
            e += 1
        return 0
