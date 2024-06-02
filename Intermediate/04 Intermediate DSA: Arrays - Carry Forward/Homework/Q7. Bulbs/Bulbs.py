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

'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        state = 0
        switchCount = 0

        for i in range(len(A)):
            if A[i] == state:
                switchCount += 1
                state = 1-state
        return switchCount
'''