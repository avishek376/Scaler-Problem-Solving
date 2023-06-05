class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i<n:
            if A[i]<1 or A[i]>n or i == A[i]-1:
                i += 1
            else:
                indx = A[i]-1
                if A[indx] == A[i]:
                    i += 1
                else:
                    A[i],A[indx] = A[indx],A[i]
        for i in range(n):
            if i != A[i]-1:
                return i+1
        return n+1