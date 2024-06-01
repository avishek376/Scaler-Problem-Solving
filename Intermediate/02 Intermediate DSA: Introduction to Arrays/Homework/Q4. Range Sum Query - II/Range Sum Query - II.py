class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        pfArr = [0] * len(A)
        pfArr[0] = A[0]
        lst = []
        for i in range(1, len(A)):
            pfArr[i] = A[i] + pfArr[i - 1]

        for j in B:
            L = j[0]
            R = j[1]
            if L == 0:
                lst.append(pfArr[R])
            else:
                lst.append(pfArr[R] - pfArr[L - 1])

        return lst


'''class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        for i in range(len(B)):
            s = 0
            for j in range(B[i][0], B[i][1] + 1):
                s += A[j]
            ans.append(s)
        return ans'''