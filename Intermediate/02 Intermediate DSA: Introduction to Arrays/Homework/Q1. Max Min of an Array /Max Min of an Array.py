class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = A[0]
        mn = A[-1]
        for i in range(1,len(A)):
            if A[i] > mx:
                mx = A[i]
        for i in range(len(A)-1):
            if A[i]<mn:
                mn = A[i]
        return mx + mn