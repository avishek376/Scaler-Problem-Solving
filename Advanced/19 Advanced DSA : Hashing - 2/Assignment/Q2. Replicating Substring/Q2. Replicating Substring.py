class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(B)
        map = {}
        for i in range(n):
            if B[i] not in map:
                map[B[i]] = 1
            else:
                map[B[i]] += 1

        for k in map:
            if map[k] % A != 0:
                return -1
        return 1
