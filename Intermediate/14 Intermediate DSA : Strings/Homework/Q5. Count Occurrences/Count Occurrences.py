class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        for i in range(n-2):
            if A[i:i+len("bob")] == "bob":
                count += 1
        return count
 