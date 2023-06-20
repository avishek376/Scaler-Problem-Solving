class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):

        length = len(A)
        ans = 0
        hashset = set()

        # using two pointers approach with hashset

        i = 0
        j = 0

        while j < length:
            # we will insert element to hashset, update the value of j and update ans.
            if A[j] not in hashset:
                hashset.add(A[j])
                j += 1
                ans = max(ans, len(hashset))
            else:  # we have to remove element from hashset and update i
                hashset.remove(A[i])
                i += 1

        return ans