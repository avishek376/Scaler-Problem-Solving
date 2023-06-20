class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if len(A) != len(B):
            return 0

        mapAB, mapBA = {}, {}

        for c1, c2 in zip(A, B):
            if (c1 in mapAB and mapAB[c1] != c2) or (c2 in mapBA and mapBA[c2] != c1):
                return 0
            mapAB[c1] = c2
            mapBA[c2] = c1
        return 1
