class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        n = A
        ret = [[0] * n for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        direction = 0
        num = 1
        while top <= bottom and left <= right:
            if direction == 0:
                # move right
                for i in range(left, right + 1):
                    ret[top][i] = num
                    num += 1
                top += 1
                direction = 1
            elif direction == 1:
                # move down
                for i in range(top, bottom + 1):
                    ret[i][right] = num
                    num += 1
                right -= 1
                direction = 2
            elif direction == 2:
                # move left
                for i in range(right, left - 1, -1):
                    ret[bottom][i] = num
                    num += 1
                bottom -= 1
                direction = 3
            else:
                # move up
                for i in range(bottom, top - 1, -1):
                    ret[i][left] = num
                    num += 1
                left += 1
                direction = 0
        return ret
