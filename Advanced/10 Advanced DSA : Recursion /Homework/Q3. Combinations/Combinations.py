class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        def comSum(ind, k, ds, n, res):
            if ind == n + 1:
                if k == len(ds):
                    res.append(ds.copy())
                return
            ds.append(ind)
            comSum(ind + 1, k, ds, n, res)
            ds.pop()
            comSum(ind + 1, k, ds, n, res)

        ds = []
        res = []

        comSum(1, B, ds, A, res)
        return res

