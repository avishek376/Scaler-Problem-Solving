class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        min1 = -10 ** 8
        sum1 = sum2 = 0
        s = 0
        e = len(A) - B

        for i in range(len(A)):
            sum1 += A[i]

        for i in range(s, e):
            sum2 += A[i]
        min1 = sum2
        s += 1

        while e < len(A):
            sum2 += A[e] - A[s - 1]
            min1 = min(min1, sum2)
            s += 1
            e += 1

        return sum1 - min1
