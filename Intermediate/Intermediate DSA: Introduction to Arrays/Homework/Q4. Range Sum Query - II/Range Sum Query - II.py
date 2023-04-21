class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        for i in range(len(B)):
            s = 0
            for j in range(B[i][0], B[i][1] + 1):
                s += A[j]
            ans.append(s)
        return ans