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
                    val = pref[j]
                else:
                    val = pref[j] - pref[i - 1]
                if val < B: ans += 1
        return ans

    '''
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
    '''
