class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        # b = len(B)
        min_total = 1000000000
        for i in range(n):
            miniLeft = 1000000000
            miniRight = 1000000000
            for j in range(i-1, -1, -1):
                if A[j] < A[i]:
                    sumLeft = B[i]+B[j]
                    miniLeft = min(miniLeft, sumLeft)
            for j in range(i+1, n):
                if A[j] > A[i]:
                    sumRight = B[j]
                    miniRight = min(miniRight, sumRight)
            min_total = min(min_total, miniRight+miniLeft)
        if min_total == 1000000000:
            return -1
        else:
            return min_total

