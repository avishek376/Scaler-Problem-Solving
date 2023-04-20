class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        switchCount = 0

    for b in A:
        if switchCount % 2 == 0:
            b = b
        else:
            b = 1 - b

        if b == 1:
            continue
        else:
            switchCount += 1
    return switchCount