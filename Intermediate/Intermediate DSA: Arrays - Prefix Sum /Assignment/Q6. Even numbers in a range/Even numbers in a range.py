class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        summ = 0
        pf = []
        res = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                resp = 1
            else:
                resp = 0
            summ += resp
            pf.append(summ)
        for i in B:
            L = i[0]
            R = i[-1]
            if L == 0:
                res.append(pf[R])
            else:
                res.append(pf[R] - pf[L - 1])

        return res


