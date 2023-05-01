class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mini = maxi = -1
        n = len(A)
        result = n
        minv = min(A)
        maxv = max(A)
        for i in range(n - 1, -1, -1):
            if A[i] == minv:
                mini = i
                if maxi != -1:
                    result = min(result, maxi - mini + 1)
            if A[i] == maxv:
                maxi = i
                if mini != -1:
                    result = min(result, mini - maxi + 1)
        return result

