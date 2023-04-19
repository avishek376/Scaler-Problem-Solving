class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        res = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                res.append(A[i:j])

        return res
