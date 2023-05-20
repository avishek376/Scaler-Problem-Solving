class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(B)  # solution with Set
        mySet = set()
        for i in range(n):
            a = B[i]
            b = A - B[i]
            if b in mySet:
                return 1
            else:
                mySet.add(B[i])
        return 0


