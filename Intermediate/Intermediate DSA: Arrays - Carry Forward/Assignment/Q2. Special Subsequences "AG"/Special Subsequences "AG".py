class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        result = 0
        n = len(A)
        factor = (10**9 + 7)
        for i in range(n-1, -1, -1):
            if A[i] == 'G':
                count += 1
            if A[i] == 'A':
                result += count
        return result%factor
