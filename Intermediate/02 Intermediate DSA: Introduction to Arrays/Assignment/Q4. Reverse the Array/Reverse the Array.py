class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        lst = []
        for i in range(len(A) - 1, -1, -1):
            lst.append(A[i])
        return lst

    '''
        if A is a list instead of tuple and we don't
        have to return a different array instead of same array
        def solve(A):
            i = 0
            j = len(A)-1
            while i<j:
                A[i],A[j] = A[j],A[i]
                i += 1
                j -= 1
        
            return A
    
    '''
    '''
        def solve(A):
            lst = [0]*len(A)
            for item in range(len(A)-1,-1,-1):
                lst[item] = A[len(A)-item-1]
            return lst
    '''
