class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        p1 = p2 = p3 = 0
        res = [0] * (n + m)

        while p1 < n and p2 < m:
            if A[p1] < B[p2]:
                res[p3] = A[p1]
                p3 += 1
                p1 += 1
            else:
                res[p3] = B[p2]
                p2 += 1
                p3 += 1
        while p1 < n:
            res[p3] = A[p1]
            p3 += 1
            p1 += 1
        while p2 < m:
            res[p3] = B[p2]
            p3 += 1
            p2 += 1

        return res