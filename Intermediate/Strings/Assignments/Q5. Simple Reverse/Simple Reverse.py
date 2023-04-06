class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        mystr = ""
        for i in range(n-1,-1,-1):
            mystr += A[i]
        return mystr