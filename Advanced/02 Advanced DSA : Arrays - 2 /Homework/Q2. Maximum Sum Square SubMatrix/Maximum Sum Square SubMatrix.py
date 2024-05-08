class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        N = len(A[0])

        # creating pf
        pf = [[0] * N for i in range(N)]

        # row-wise pf
        for i in range(N):
            for j in range(N):
                if i == 0:
                    pf[i][j] = A[i][j]
                else:
                    pf[i][j] = pf[i - 1][j] + A[i][j]

        # col-wise pf
        for i in range(N):
            for j in range(N):
                if j == 0:
                    continue
                else:
                    pf[i][j] = pf[i][j - 1] + pf[i][j]

        max_sum = float('-inf')

        # sliding window
        for x in range(N - B + 1):
            for y in range(N - B + 1):
                a1, b1 = x, y
                a2, b2 = x + B - 1, y + B - 1

                cur_sum = pf[a2][b2]

                if a1 > 0:
                    cur_sum -= pf[a1 - 1][b2]

                if b1 > 0:
                    cur_sum -= pf[a2][b1 - 1]

                if a1 > 0 and b1 > 0:
                    cur_sum += pf[a1 - 1][b1 - 1]

                max_sum = max(max_sum, cur_sum)

        return max_sum
