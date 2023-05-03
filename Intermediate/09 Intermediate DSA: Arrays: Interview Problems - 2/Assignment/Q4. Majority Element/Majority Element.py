class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        ele = A[0]
        freq = 1
        for i in range(1,n):
            if freq == 0:
                ele = A[i]
                freq = 1
            elif ele == A[i]:
                freq += 1
            else:
                freq -= 1
        c = 0
        # concluding count of majority ele.
        for i in range(n):
            if A[i] == ele:
                c += 1
        if c > n//2:
            return ele
        else:
            return -1