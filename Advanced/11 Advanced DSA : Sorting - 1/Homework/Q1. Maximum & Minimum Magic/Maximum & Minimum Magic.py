class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        maxAns = minAns = 0
        n = len(A)
        B = []
        mod = 1000000007
        for i in range(0, n, 2):
            minAns = (minAns + (abs(A[i] - A[i + 1]))) % mod

        for i in range(0, n // 2):
            maxAns = (maxAns + (abs(A[i] - A[n - i - 1]))) % mod

        B.append(maxAns)
        B.append(minAns)
        return B
