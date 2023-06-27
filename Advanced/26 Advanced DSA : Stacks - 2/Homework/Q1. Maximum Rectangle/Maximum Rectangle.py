class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        def leftSmallerA(A):
            n = len(A)

            nseOnLeft = [-1 for i in range(n)]
            stckLeft = []
            for i in range(n - 1, -1, -1):
                while len(stckLeft) > 0 and A[stckLeft[-1]] > A[i]:
                    nseOnLeft[stckLeft.pop()] = i
                stckLeft.append(i)
            return nseOnLeft

        def rightSmallerA(A):
            n = len(A)
            nseOnRight = [n for i in range(n)]
            stckRight = []
            for i in range(n):
                while len(stckRight) > 0 and A[stckRight[-1]] > A[i]:
                    nseOnRight[stckRight.pop()] = i
                stckRight.append(i)
            return nseOnRight

        def maxAreaHistogram(A):
            N = len(A)
            maxArea = 0
            leftSmaller = leftSmallerA(A)
            rightSmaller = rightSmallerA(A)
            for i in range(N):
                currArea = A[i] * (rightSmaller[i] - leftSmaller[i] - 1)
                maxArea = max(maxArea, currArea)
            return maxArea

        N = len(A)
        M = len(A[0])
        currRow = A[0]
        maxArea = maxAreaHistogram(currRow)

        for i in range(1, N):
            for j in range(M):
                if A[i][j] == 1:
                    currRow[j] += 1
                else:
                    currRow[j] = 0

            currArea = maxAreaHistogram(currRow)
            maxArea = max(maxArea, currArea)

        return maxArea
