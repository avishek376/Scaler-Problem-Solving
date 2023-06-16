class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        A.sort()
        i, j = 0, 1
        ans = 0
        while(j < n):
            if(j == i):
                j += 1
                continue
            x, y = A[i], A[j]
            if(y - x == B):
                # count the pair A[i], A[j] only once
                ans += 1
                while(i < n and A[i] == x):
                    i += 1
                while(j < n and A[j] == y):
                    j += 1
            elif(y - x > B):
                i += 1
            else:
                j += 1
        return ans