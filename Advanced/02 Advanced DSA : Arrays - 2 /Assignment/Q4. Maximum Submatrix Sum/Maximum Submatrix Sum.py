class Solution:
    # @param A : list of list of integers
    # @return an long
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        pfMat = [[0] * M for _ in range(N)]

        # row wise sum
        for i in range(N):
            for j in range(M):
                if j == 0:
                    pfMat[i][j] = A[i][j]
                else:
                    pfMat[i][j] = pfMat[i][j - 1] + A[i][j]

                    # col wise sum
        for j in range(M):
            for i in range(1, N):
                pfMat[i][j] = pfMat[i - 1][j] + pfMat[i][j]

        maxi = -10 ** 8
        x2 = N - 1
        y2 = M - 1
        # checking all the posibilities of finding TL and max
        for i in range(N):
            for j in range(M):

                x1 = i
                y1 = j
                summ = 0

                summ += pfMat[x2][y2]
                if x1 > 0:
                    summ -= pfMat[x1 - 1][y2]
                if y1 > 0:
                    summ -= pfMat[x2][y1 - 1]
                if x1 > 0 and y1 > 0:
                    summ += pfMat[x1 - 1][y1 - 1]

                maxi = max(maxi, summ)
        return maxi
