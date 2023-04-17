class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        R = []
        k = len(A)
        for i in range(len(B)):
            x = B[i] % k
            R.append(A[x:] + A[:x])

        return R
