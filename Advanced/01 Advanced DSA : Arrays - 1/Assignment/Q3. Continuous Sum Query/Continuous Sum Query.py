class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = A
        coins = [0 for __ in range(n)]

        for i in range(len(B)):
            leftIndex = B[i][0] - 1
            rightIndex = B[i][1] - 1
            donationByDevotee = B[i][2]
            coins[leftIndex] += donationByDevotee
            if (rightIndex + 1) < n:
                coins[rightIndex + 1] -= donationByDevotee
        summ = 0
        pf = []
        for i in range(n):
            summ += coins[i]
            pf.append(summ)
        return pf

