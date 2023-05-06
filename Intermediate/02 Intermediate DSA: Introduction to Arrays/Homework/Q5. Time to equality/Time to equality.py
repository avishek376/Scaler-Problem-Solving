class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = max(A)
        count = 0
        for i in range(len(A)):
            if A[i] == mx:
                pass
            else:
                count+=mx-A[i]
        return count

