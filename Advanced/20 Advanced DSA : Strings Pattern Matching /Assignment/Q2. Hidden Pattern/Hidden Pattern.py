class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        def getLPS(lpsArr, string):
            n = len(lpsArr)
            for i in range(1, n):
                x = lpsArr[i - 1]
                while string[i] != string[x]:
                    if x == 0:
                        x = -1
                        break
                    x = lpsArr[x - 1]

                lpsArr[i] = x + 1
            return lpsArr

        string = B + "@" + A
        lpsArr = [0] * (len(string))
        getLPS(lpsArr, string)
        occurCount = 0
        for i in range(len(lpsArr)):
            if lpsArr[i] == len(B):
                occurCount += 1
        return occurCount