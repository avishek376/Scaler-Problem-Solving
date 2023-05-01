class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        res = []
        n = len(A)
        lsto = [0 for _ in range(n)]

        lsto[0] = 0
        for i in range(1, n):
            if i % 2 != 0:
                lsto[i] = (lsto[i - 1] + A[i])
            else:
                lsto[i] = (lsto[i - 1])

        for j in B:
            L = j[0]
            R = j[-1]
            if L == 0:
                res.append(lsto[R])
            else:
                res.append(lsto[R] - lsto[L - 1])

        return res
