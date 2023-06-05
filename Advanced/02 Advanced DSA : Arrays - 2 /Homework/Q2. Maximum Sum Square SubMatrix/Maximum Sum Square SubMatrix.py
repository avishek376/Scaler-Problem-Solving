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
            prev = A[i][0]
            pf[i][0] = A[i][0]
            for j in range(1, N):
                pf[i][j] = prev + A[i][j]
                prev = pf[i][j]

        # col-wise pf
        for k in range(N):
            prev = pf[0][k]
            for i in range(1, N):
                pf[i][k] = prev + pf[i][k]
                prev = pf[i][k]

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