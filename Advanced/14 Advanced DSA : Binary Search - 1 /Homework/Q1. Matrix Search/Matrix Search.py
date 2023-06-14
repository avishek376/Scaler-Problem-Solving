class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        def checkNum(Arr, K):
            # print(A,"==>",K)
            s = 0
            n = len(Arr)
            e = n - 1
            while s <= e:
                mid = e + (s - e) // 2
                if Arr[mid] == K:
                    return True
                elif Arr[mid] > K:
                    e = mid - 1
                elif Arr[mid] < K:
                    s = mid + 1
            return False

        for i in range(len(A)):
            if checkNum(A[i], B):
                return 1

        return 0
