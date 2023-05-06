class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        lst = []
        for i in range(len(A)-1, -1, -1):
            lst.append(A[i])
        return lst

    '''
        def solve(A):
            lst = [0]*len(A)
            for item in range(len(A)-1,-1,-1):
                lst[item] = A[len(A)-item-1]
            return lst
    '''



