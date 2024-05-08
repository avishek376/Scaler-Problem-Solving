class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            # if the value is out of range or already in the correct place then move forward
            if A[i] < 1 or A[i] > n or i == A[i] - 1:
                i += 1
            else:
                # find the actual index of the value in 0 based indexing.
                indx = A[i] - 1
                # for duplicate scenarios. If the already one instance of the value is not present then swap else move forward
                if A[indx] == A[i]:
                    i += 1
                else:
                    # don't increase the counter as the value at the current index is not in the correct place...
                    A[i], A[indx] = A[indx], A[i]
        for i in range(n):
            if i != A[i] - 1:
                return i + 1
        return n + 1
