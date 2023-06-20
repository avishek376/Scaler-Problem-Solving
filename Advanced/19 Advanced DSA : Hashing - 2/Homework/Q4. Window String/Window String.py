class Solution:
    # @param A : string
    # @param B : string
    # @return a string
    def minWindow(self, A, B):
        counts = {c: 0 for c in B}
        target_counts = {}
        # stores the frequency of all character in B
        for c in B:
            if c in target_counts:
                target_counts[c] += 1
            else:
                target_counts[c] = 1
        cover = 0
        shortest = None
        start, end = 0, 0
        while end < len(A) or cover == len(counts):
            if cover < len(counts):
                end += 1
                if A[end - 1] in counts:
                    # We check if the current character represented by end caused a character
                    # to be included which is relevant to B and is still in deficit.
                    if counts[A[end - 1]] == target_counts[A[end - 1]] - 1:
                        cover += 1
                    counts[A[end - 1]] += 1
            else:
                # move the start pointer popping out the character that
                # still makes sure that all characters in B are covered.
                if A[start] in counts:
                    counts[A[start]] -= 1
                    if counts[A[start]] == target_counts[A[start]] - 1:
                        cover -= 1
                start += 1
            # check if we have all characters in B covered
            if cover == len(counts):
                if shortest is None or end - start < shortest[0]:
                    shortest = end - start, start, end
        if shortest is None:
            return ""
        return A[shortest[1] : shortest[2]]