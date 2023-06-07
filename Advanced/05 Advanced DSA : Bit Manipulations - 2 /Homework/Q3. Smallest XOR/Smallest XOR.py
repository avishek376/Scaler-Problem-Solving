class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        X = A
        countSetBitsX = 0
        for i in range(32):
            if X & (1 << i):
                countSetBitsX += 1
        # print(countSetBitsX)

        # edge case
        if countSetBitsX == B: return A

        if countSetBitsX > B:
            for i in range(32):
                if X & (1 << i):
                    X = X ^ (1 << i)
                    countSetBitsX -= 1
                if countSetBitsX == B:
                    break
        else:
            for i in range(32):
                if X & (1 << i) == 0:
                    X = X ^ (1 << i)
                    countSetBitsX += 1
                if countSetBitsX == B:
                    break
        return X

'''
class Solution:
    def solve(self, A, B):
        x = 0
        for i in range(30, -1, -1):
            if B == 0:
                return x
            if (1 << i) & A:
                x |= 1 << i
                B -= 1
        for i in range(31):
            if B == 0:
                return x
            if ((1 << i) & x) == 0:
                x |= 1 << i
                B -= 1
        return x

'''