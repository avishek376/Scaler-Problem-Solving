class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        pf = []
        summ = 0
        for i in range(n):
            summ += A[i]
            pf.append(summ)

        dict1 = {}
        count = 0
        for i in range(n):
            if pf[i] == B:
                count += 1
            if pf[i] - B in dict1:
                count += dict1[pf[i] - B]
            if pf[i] in dict1:
                dict1[pf[i]] += 1
            else:
                dict1[pf[i]] = 1
        return count
