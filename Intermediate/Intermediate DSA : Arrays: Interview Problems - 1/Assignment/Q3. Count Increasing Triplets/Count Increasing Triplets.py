class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        for i in range(n):
            l = 0
            r = 0
            for j in range(i - 1, -1, -1):
                if A[j] < A[i]:
                    l += 1
            for j in range(i + 1, n):
                if A[j] > A[i]:
                    r += 1
            ans += l * r

        return ans
