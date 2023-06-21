class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def reverseString(A):
            n = len(A)
            str = ""
            for i in range(n - 1, -1, -1):
                str += A[i]
            return str

        def getLPS(s):
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

        revString = reverseString(A)
        if revString == A:
            return 0
        text = A + "@" + revString
        lpsArray = []
        lpsArray = getLPS(text)
        N = len(A)

        return N - lpsArray[-1]


