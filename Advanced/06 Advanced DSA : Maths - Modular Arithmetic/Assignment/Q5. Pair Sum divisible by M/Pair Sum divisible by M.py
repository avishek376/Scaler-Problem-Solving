class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        countArr = [0] * B
        mod = 10 ** 9 + 7
        count = 0
        # step -1
        # create a count array by taking modulo of all ele and by add their freq
        modVal = 0
        n = len(A)
        for i in range(n):
            modVal = A[i] % B
            countArr[modVal] += 1
        # step-2
        # handle the edge cases for 0 and m/2 if exists
        x = countArr[0]
        count += (x * (x - 1)) // 2

        if B % 2 == 0:
            y = countArr[B // 2]
            count += (y * (y - 1)) // 2
        # step-3
        # count the pairs
        s = 1
        e = B - 1
        while s < e:
            count += countArr[s] * countArr[e]
            s += 1
            e -= 1

        return count % mod
