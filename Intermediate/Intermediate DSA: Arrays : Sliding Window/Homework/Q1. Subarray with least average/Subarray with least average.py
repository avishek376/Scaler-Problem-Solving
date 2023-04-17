class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        summ = 0
        K = B
        n = len(A)
        for i in range(K):
            summ += A[i]
        s = 1
        e = K
        ans = summ
        res_index = 0
        while e<n :
            summ = summ - A[s-1]+A[e]
            if ans > summ:
                ans = summ
                res_index = s

            s += 1
            e += 1
        return res_index