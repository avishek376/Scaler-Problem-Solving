class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        i = 0
        j = cols -1
        # indx = 10001
        while i < rows and j >= 0:
            while A[i][j] == 1 and j >= 0:
                index = i
                j -= 1
            i += 1

        return index
