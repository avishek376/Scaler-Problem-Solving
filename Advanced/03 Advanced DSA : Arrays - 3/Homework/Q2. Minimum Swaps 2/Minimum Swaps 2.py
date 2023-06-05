class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        swapCount = 0
        for i in range(len(A)):
            while A[i] != i:
                indx = A[i]
                A[i],A[indx] = A[indx],A[i]
                swapCount += 1
        return swapCount


'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        i = 0
        swapCount = 0
        while i < len(A):
            if A[i] == i:
                i+=1
            else:
                dstn = A[i]
                src = i
                A[src],A[dstn] = A[dstn],A[src]
                swapCount +=1

        return swapCount
        '''