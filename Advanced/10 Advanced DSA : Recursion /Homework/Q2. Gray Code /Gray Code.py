class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1 :
            base = []
            base.append(0)
            base.append(1)
            return base
        rres = self.grayCode(A-1)
        mres = []
        for i in range(0, len(rres)) :
            mres.append(rres[i])
        for i in range(len(rres)-1, -1, -1) :
            mres.append((1<<(A-1)) + rres[i])
        return mres
