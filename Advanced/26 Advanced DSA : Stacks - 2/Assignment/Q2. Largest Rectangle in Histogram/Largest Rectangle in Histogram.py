class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        n = len(A)

        maxArea = -10 ** 8
        nseOnLeft = [-1 for i in range(n)]
        stckLeft = []
        for i in range(n - 1, -1, -1):
            while len(stckLeft) > 0 and A[stckLeft[-1]] > A[i]:
                nseOnLeft[stckLeft.pop()] = i
            stckLeft.append(i)

        nseOnRight = [n for i in range(n)]
        stckRight = []
        for i in range(n):
            while len(stckRight) > 0 and A[stckRight[-1]] > A[i]:
                nseOnRight[stckRight.pop()] = i
            stckRight.append(i)

        for i in range(n):
            width = nseOnRight[i] - nseOnLeft[i] - 1
            maxArea = max(maxArea, A[i] * width)
        return maxArea
