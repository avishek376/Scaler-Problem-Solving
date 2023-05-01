class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        pfe = [0 for i in range(n)]
        pfo = [0 for i in range(n)]

        pfe[0] = A[0]
        for i in range(1, n):
            if i % 2 == 0:
                pfe[i] = (pfe[i - 1] + A[i])
            else:
                pfe[i] = (pfe[i - 1])
      

        pfo[0] = 0
        for i in range(1, n):
            if i % 2 != 0:
                pfo[i] = (pfo[i - 1] + A[i])
            else:
                pfo[i] = (pfo[i - 1])


        c = 0

        for i in range(n):
            se = pfo[n - 1] - pfo[i]
            if i > 0:
                se = se + pfe[i - 1]
            so = pfe[n - 1] - pfe[i]
            if i > 0:
                so = so + pfo[i - 1]
            if se == so:
                c += 1
        return c
