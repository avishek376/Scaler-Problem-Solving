class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()

        for i in range(n - 2):
            # print(A[i+1],"<<==>>",A[i],"<<=>>",A[i+2])
            if A[i + 1] - A[i] != A[i + 2] - A[i + 1]:
                return 0
        return 1
