class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort(reverse=True)

        less = 0
        if A[0] == 0:
            return 1
        for i in range(1, n):
            if A[i] != A[i - 1]:
                less = i

            if less == A[i]:
                return 1
        return -1
