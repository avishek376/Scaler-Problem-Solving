class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def createLps(s):
            m = len(s)
            lps = [0] * m
            for i in range(1, m):
                x = lps[i - 1]
                while (s[i] != s[x]):
                    if x == 0:
                        x = -1
                        break
                    x = lps[x - 1]

                lps[i] = x + 1

            return lps

        lps = createLps(A)
        if lps[len(A) - 1] == 0:
            return len(A)
        else:
            return len(A) - max(lps)
