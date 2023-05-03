class Solution:
    # @param A : list of integers
    # @return a strings

    def solve(self, A):
        cnt = 0
        for val in A:
            if val % 2:
                cnt += 1
        # checks the parity of the number of odd elements
        if cnt % 2 == 0:
            return "Yes"
        else:
            return "No"

    '''def solve(self, A):
        summ = 0
        for i in range(len(A)):
            summ = summ^A[i]

        if summ % 2 == 0:
            return "Yes"
        else:
            return "No"'''
