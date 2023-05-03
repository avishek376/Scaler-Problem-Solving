class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long

    def solve(self, A, B):
        count = 0
        zeroes = 0
        N = A

        for i in range(len(B)):
            if B[i] == 0:
                zeroes += 1
            else:
                count += (zeroes * (zeroes + 1)) // 2
                zeroes = 0

        count += (zeroes * (zeroes + 1)) // 2

        return (N * (N + 1)) // 2 - count

    '''def solve(self, A, B):
        ans, res = 0, 0
        for i in range(A):
            if B[i] == 1:
                res = i + 1
            ans += res
        return ans'''
