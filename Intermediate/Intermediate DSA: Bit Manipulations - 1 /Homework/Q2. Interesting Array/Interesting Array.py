class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        summ = 0
        for i in range(len(A)):
            summ = summ^A[i]

        if summ % 2 == 0:
            return "Yes"
        else:
            return "No"
