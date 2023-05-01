class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        res = [[0]*rows for k in range(cols)]
        for i in range(rows):
            for j in range(cols):
                res[j][i] = A[i][j]
        return res


    '''
    def solve(self, A):
        ans = []
        # Iterating over the columns
        for i in range(0,len(A[0])):
            temp = []
            # Iterating over the rows
            for j in range(0,len(A)):
                temp.append(A[j][i])
            ans.append(temp)
        return ans
    '''
