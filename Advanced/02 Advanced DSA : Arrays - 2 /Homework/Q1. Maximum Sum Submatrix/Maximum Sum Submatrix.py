def kadane(v):
    currSum = 0
    maxSum = -1e9
    for i in range(len(v)):
        currSum += v[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0: currSum = 0
    return maxSum


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        r = len(A)
        c = len(A[0])
        prefix = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if j == 0:
                    prefix[i][j] = A[i][j]
                else:
                    prefix[i][j] = prefix[i][j - 1] + A[i][j]
        maxSum = -1e9
        for i in range(c):
            for j in range(i, c):
                v = []
                for k in range(r):
                    el = 0
                    if i == 0:
                        el = prefix[k][j]
                    else:
                        el = prefix[k][j] - prefix[k][i - 1]
                    v.append(el)
                maxSum = max(maxSum, kadane(v))
        return maxSum


'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        def kadanes(arr):
            summ = 0
            ans = -10 ** 8
            for i in range(len(arr)):
                if summ >= 0:
                    summ += arr[i]
                else:
                    summ = arr[i]
                ans = max(ans, summ)
            return ans

        maxi = -10 ** 8
        for k in range(cols):
            pfArr = [0 for __ in range(rows)]
            for j in range(k, cols):
                for i in range(rows):
                    pfArr[i] = (A[i][j]) + pfArr[i]
                currMax = kadanes(pfArr)
                maxi = max(maxi, currMax)

        return maxi
'''
