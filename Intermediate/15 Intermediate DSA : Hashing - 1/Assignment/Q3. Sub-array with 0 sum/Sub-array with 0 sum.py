class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        pfSum = [A[0]]
        # Calculate pfSum
        for index in range(1, N):
            pfSum.append(pfSum[index-1]+A[index])
        # Checking subarray of sum equals to 0 present or not
        hashset = set(pfSum)
        if len(hashset) != N:
            return 1
        if 0 in hashset:
            return 1
        return 0