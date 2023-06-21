class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        def lpsBuilder(text):
            n = len(text)

            lps = [0] * n

            for i in range(1, n):

                x = lps[i - 1]
                while (text[i] != text[x]):

                    if x == 0:
                        x -= 1
                        break

                    x = lps[x - 1]

                lps[i] = x + 1

            return lps

        text = A + '@' + B + B
        lps = lpsBuilder(text)

        result = 0

        for no in lps:
            if no == len(A):
                result += 1

        return result - 1 if A == B else result




