from collections import OrderedDict

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        h1 = OrderedDict()
        h2 = OrderedDict()
        # stores the frequency of the elements of A
        for x in A:
            if x in h1:
                h1[x] += 1
                continue
            h1[x] = 1
        # stores the frequency of the elements of B
        for y in B:
            if y in h2:
                h2[y] += 1
                continue
            h2[y] = 1
        a = []
        for k, freq in h2.items():
            if k in h1:
                t = h1[k]
                while t > 0:
                    a.append(k)
                    t = t - 1
                del h1[k]
        res = sorted(h1.items())
        # append the elements that are not present in B
        for k, item in res:
            while item:
                a.append(k)
                item -= 1
        return a