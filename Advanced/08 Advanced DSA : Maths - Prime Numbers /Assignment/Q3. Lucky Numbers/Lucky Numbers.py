class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        spf = [0 for _ in range(A + 1)]
        spf[0] = spf[1] = -1

        limit = int((A / 2) + 1)

        for i in range(2, limit):
            if spf[i] == 0:
                for j in range(i * 2, A + 1, i):
                    spf[j] += 1
                    # print(spf)
        count = 0
        for i in range(len(spf)):
            if spf[i] == 2:
                count += 1
        return count