class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        countChunks = 0
        maxi = -10 ** 8
        for i in range(n):
            maxi = max(maxi, A[i])
            if (maxi == i):
                countChunks += 1

        return countChunks
