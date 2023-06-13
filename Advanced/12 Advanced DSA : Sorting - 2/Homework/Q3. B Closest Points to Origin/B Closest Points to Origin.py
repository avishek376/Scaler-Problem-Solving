from functools import cmp_to_key


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)

        def compareDistance(p1, p2):

            d1 = (p1[0] * p1[0] + p1[1] * p1[1])
            d2 = (p2[0] * p2[0] + p2[1] * p2[1])

            if d1 > d2:
                return 1
            elif d1 == d2:
                return 0
            elif d1 < d2:
                return -1

        A.sort(key=cmp_to_key(compareDistance))

        res = []

        for i in range(B):
            res.append(A[i])

        return res

'''
by Min-Heap

import heapq as hq
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, points, k):
        N = len(points)
       
        min_heap = []
       
        for i in range(N):
            sqrt = ( points[i][0] * points[i][0] ) + (points[i][1] * points[i][1])
            hq.heappush(min_heap, (sqrt,points[i]))
           
           
        ans = []
        while k > 0:
            val , point = hq.heappop(min_heap)
            ans.append(point)
            k -= 1
           
        return ans
'''