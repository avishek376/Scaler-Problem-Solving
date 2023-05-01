class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count1 = 0
        count2 = 0
        ele1 = -1
        ele2 = -1
        n = len(A)
        for i in range(n):
            if A[i] == ele1:
                count1 += 1
            elif A[i] == ele2:
                count2 += 1
            elif count1 == 0:
                ele1 = A[i]
                count1 = 1
            elif count2 == 0:
                ele2 = A[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        cele1 = 0
        cele2 = 0
        for j in range(n):
            if A[j] == ele1:
                cele1 += 1
        for k in range(n):
            if A[k] == ele2:
                cele2 += 1
        if cele1 > n // 3:
            return ele1
        elif cele2 > n // 3:
            return ele2
        return -1
