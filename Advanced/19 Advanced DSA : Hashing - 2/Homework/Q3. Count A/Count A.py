class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        for i in range(n-1,-1,-1):
            if A[i] == 'a':
                count += 1
        count = count*(count+1)//2
        return count
