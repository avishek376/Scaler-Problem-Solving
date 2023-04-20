class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        mx = A[n - 1]
        lst = [mx]
        for i in range(n - 2, -1, -1):
            if A[i] > mx:
                mx = A[i]
                lst.append(A[i])
        return lst
