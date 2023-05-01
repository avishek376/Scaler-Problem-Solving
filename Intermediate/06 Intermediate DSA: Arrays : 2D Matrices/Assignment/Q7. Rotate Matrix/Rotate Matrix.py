class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)

        # STEP-1 ==> TRANSPOSE THE MATRIX
        for i in range(n):
            for j in range(n):
                if i < j:
                    temp = A[i][j]
                    A[i][j] = A[j][i]
                    A[j][i] = temp
                if i == j:
                    pass
        # STEP-2 ==> REVERSE THE ROW
        for k in range(n):
            last = n - 1
            for l in range(0, n // 2):
                trmp = A[k][last]
                A[k][last] = A[k][l]
                A[k][l] = trmp
                last -= 1

        return A
