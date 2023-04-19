class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        pref = [0] * (n)
        pref[0] = A[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + A[i]
        ans = 0
        for i in range(n):
            for j in range(i, n):

                if i == 0:
                    sum = pref[j]
                else:
                    sum = pref[j] - pref[i - 1]
                sz = j - i + 1
                if sz % 2 == 0 and sum < B: ans += 1
                if sz & 1 and sum > B: ans += 1
        return ans

