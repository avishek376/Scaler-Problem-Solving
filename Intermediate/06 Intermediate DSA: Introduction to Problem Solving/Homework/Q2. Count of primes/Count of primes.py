class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0

        for num in range(A + 1):
            j = 2
            if num <= 1:
                continue
            while j * j <= num:
                if (num % j) == 0:
                    break
                j += 1
            else:
                count += 1

        return count
