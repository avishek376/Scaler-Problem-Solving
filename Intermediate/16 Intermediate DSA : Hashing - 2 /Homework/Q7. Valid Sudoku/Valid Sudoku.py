class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        occurrence = set()

        for i in range(0, 9):
            for j in range(0, 9):
                if A[i][j] != '.':
                    cur = A[i][j]
                    if (i, cur) in occurrence or (cur, j) in occurrence or (i // 3, j // 3, cur) in occurrence:
                        return 0
                    occurrence.add((i, cur))
                    occurrence.add((cur, j))
                    occurrence.add((i // 3, j // 3, cur))

        return 1
