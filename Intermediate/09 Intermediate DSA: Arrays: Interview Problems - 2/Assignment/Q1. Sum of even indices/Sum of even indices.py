class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        res = []
        n = len(A)
        lste = [0 for _ in range(n)]

        lste[0] = A[0]
        for i in range(1, n):
            if i % 2 == 0:
                lste[i] = (lste[i - 1] + A[i])
            else:
                lste[i] = (lste[i - 1])

        for j in B:
            L = j[0]
            R = j[-1]
            if L == 0:
                res.append(lste[R])
            else:
                res.append(lste[R] - lste[L - 1])

        return res