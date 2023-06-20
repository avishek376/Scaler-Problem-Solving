class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        eleSet = set(A)

        ans = 0
        for i in eleSet:
            x = i
            prev_elem = x - 1

            if prev_elem not in eleSet:
                count = 0
                while x in eleSet:
                    x = x + 1
                    count += 1
                ans = max(ans, count)

        return ans
