class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        count = 0
        for i in range(1, n):
            
            if A[i - 1] >= A[i]:
                count += A[i - 1] + 1 - A[i]
                A[i] += A[i - 1] + 1 - A[i]

            elif A[i - 1] < A[i]:
                pass

        return count
