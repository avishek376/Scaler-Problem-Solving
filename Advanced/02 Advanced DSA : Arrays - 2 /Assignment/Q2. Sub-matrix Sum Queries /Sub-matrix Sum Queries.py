class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        N = len(A)
        M = len(A[0])
        pfMat = [[0] * M for __ in range(N)]

        for i in range(N):
            for j in range(M):
                if j == 0:
                    pfMat[i][j] = A[i][j]
                else:
                    pfMat[i][j] = pfMat[i][j - 1] + A[i][j]

        for j in range(M):
            for i in range(1, N):
                pfMat[i][j] = pfMat[i - 1][j] + pfMat[i][j]

        resultArr = []

        for q in range(len(B)):
            x1 = B[q] - 1
            y1 = C[q] - 1
            x2 = D[q] - 1
            y2 = E[q] - 1
            summ = 0
            summ += pfMat[x2][y2]

            if x1 > 0:
                summ -= pfMat[x1 - 1][y2]
            if y1 > 0:
                summ -= pfMat[x2][y1 - 1]
            if x1 > 0 and y1 > 0:
                summ += pfMat[x1 - 1][y1 - 1]

            resultArr.append(summ % (10 ** 9 + 7))
        return resultArr