class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        n = len(A)
        S = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        for i in range(n - 1, -1, -1):
            if A[i] in S:
                count += n - i
        return count % 10003

