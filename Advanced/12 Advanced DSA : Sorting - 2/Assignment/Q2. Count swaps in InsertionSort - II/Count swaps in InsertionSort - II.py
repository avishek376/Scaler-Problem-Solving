class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        n = len(A)
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    count += 1
                else:
                    break

        return count
