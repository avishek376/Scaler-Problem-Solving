class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        rows = len(A)
        cols = len(A[0])
        # set indexes for top right element
        i = 0
        j = cols - 1
        mini = 0
        ans = 10 ** 8
        while (i < rows and j >= 0):
            if (A[i][j] == B):
                mini = (i + 1) * 1009 + (j + 1)
                ans = min(mini, ans)
                j -= 1
                continue
            if (A[i][j] > B):
                j -= 1
            else:
                i += 1

        if ans == 10 ** 8:
            return -1
        return ans
