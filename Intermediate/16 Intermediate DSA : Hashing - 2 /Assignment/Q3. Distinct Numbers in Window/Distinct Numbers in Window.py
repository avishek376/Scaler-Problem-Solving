class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        N = len(A)

        myDict = {}
        lst = []
        cnt = 0

        # filling first window
        for i in range(0, B):
            if A[i] in myDict:
                myDict[A[i]] += 1
            else:
                myDict[A[i]] = 1
                cnt += 1

        lst.append(cnt)

        # for every other window, we will remove first element of previous window and add next element of array in current window
        for i in range(B, N):

            # Logic of removing first element of previous window
            myDict[A[i - B]] -= 1
            if myDict[A[i - B]] == 0:
                del myDict[A[i - B]]
                cnt -= 1

            if A[i] in myDict:
                myDict[A[i]] += 1
            else:
                myDict[A[i]] = 1
                cnt += 1

            lst.append(cnt)

        return lst
