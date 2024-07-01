class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        rows = len(A)
        cols = len(A[0])

        dpArr = [[-1] * cols for _ in range(rows)]

        def uniquePath(A, dpArr, r, c):
            if r < 0 or c < 0:
                return 0

            # for blockade/obstacle
            if A[r][c] == 1:
                dpArr[r][c] = 0
                return dpArr[r][c]

            if r == 0 and c == 0:
                dpArr[r][c] = 1
                return dpArr[r][c]

            if dpArr[r][c] != -1: return dpArr[r][c]

            a = uniquePath(A, dpArr, r - 1, c)
            b = uniquePath(A, dpArr, r, c - 1)
            dpArr[r][c] = a + b
            return a + b

        uniquePath(A, dpArr, rows - 1, cols - 1)
        return dpArr[rows - 1][cols - 1]


'''
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
        rows = len(A)
        cols = len(A[0])

        dpArr = [[-1] * cols for _ in range(rows)]

        
        def uniquePath(mat,dpArr,r,c):
            if r < 0 or c < 0:
                return 0

            if r == 0 and c == 0 and mat[r][c] == 0:
                return 1            
            elif r == 0 and c == 0 and mat[r][c] == 1:
                return 0

            if mat[r][c] == 1:
                return 0
            if dpArr[r][c] != -1:
                return dpArr[r][c]

            a = uniquePath(mat,dpArr,r-1,c)
            b = uniquePath(mat,dpArr,r,c-1)

            dpArr[r][c] = a+b
            return a+b

        return uniquePath(A,dpArr,rows-1,cols-1) 


'''