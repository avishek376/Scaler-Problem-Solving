class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        v = 0
        res = []
        n = len(A)
        for i in range(n):
            v ^= A[i]

        pos = 0
        for j in range(32):
            if v & (1 << j):
                pos = j
                break

        ans1 = 0
        ans2 = 0
        for i in range(n):
            if A[i] & 1 << pos:
                ans2 ^= A[i]
            else:
                ans1 ^= A[i]

        if ans1 > ans2:
            res.append(ans2)
            res.append(ans1)
        else:
            res.append(ans1)
            res.append(ans2)
        return res