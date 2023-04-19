class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += A[j]

                if summ < B:
                    count += 1
        return count