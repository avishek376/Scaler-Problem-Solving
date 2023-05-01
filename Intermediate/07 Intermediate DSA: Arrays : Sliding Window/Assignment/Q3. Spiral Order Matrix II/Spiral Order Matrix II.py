class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):


        mat = [ [0] * A for i in range(A) ]

        dir = 0
        k = 1
        top = 0
        bottom = A - 1
        left = 0
        right = A - 1
        while top <= bottom and left <= right:
            if dir == 0:
                # top fix
                for i in range(left, right + 1):
                    mat[top][i] = k
                    k += 1
                top += 1
            elif dir == 1:
                #right fix
                for i in range(top, bottom + 1):
                    mat[i][right] = k
                    k += 1
                right -= 1
            elif dir == 2:
                #bottom fix
                for i in range(right, left - 1, -1):
                    mat[bottom][i] = k
                    k += 1
                bottom -= 1

            elif dir == 3:
                #left fix
                for i in range(bottom, top - 1, -1):
                    mat[i][left] = k
                    k += 1
                left += 1
            dir = (dir + 1) % 4
        return mat
