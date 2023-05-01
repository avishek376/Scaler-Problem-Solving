class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i = 1
        count = 0
        while i*i <= A:
            if A % i == 0:
                if i*i == A:
                    count += 1
                else:
                    count += 2
            i += 1
        return count

