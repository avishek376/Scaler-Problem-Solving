class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        length = 2 * B + 1
        n = len(A)
        ans = []

        for i in range(n - length + 1):
            prev = -1
            flag = 1
            for j in range(i, i + length):
                if A[j] == prev:
                    flag = 0
                    break
                prev = A[j]

            if flag == 1:
                ans.append(i + B)

        return ans