class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        summ = 0

        r = 0
        c = 0
        while r<n and c<n:
            summ += A[r][c]
            r+= 1
            c+=1
        return summ


    '''
        approach 2
        class Solution:
        # @param A : tuple of list of integers
        # @return an integer
        def solve(self, A):
            n = len(A)
            summ = 0
            for i in range(n):
                for j in range(n):
                    if i == j:
                        summ += A[i][j]
            return summ
    '''
