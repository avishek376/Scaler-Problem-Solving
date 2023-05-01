class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        K = 0
        # window length
        for i in range(n):
            if A[i] <= B:
                K += 1
        swap = 0
        # first window's swap count
        for i in range(K):
            if A[i] > B:
                swap += 1
        s = 1
        e = K
        ans = swap
        while e < n:
            if A[s - 1] > B:
                swap -= 1
            if A[e] > B:
                swap += 1

            if ans > swap:
                ans = swap
            s += 1
            e += 1
        return ans