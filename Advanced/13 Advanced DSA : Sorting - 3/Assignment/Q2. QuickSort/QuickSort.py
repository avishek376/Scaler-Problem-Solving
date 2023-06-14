import sys
import random

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        self.quickSort(A, 0, n - 1)
        return A

    def quickSort(self, arr, start, end):
        if end <= start:
            return

        pos = self.rearrangeArray(arr, start, end)

        self.quickSort(arr, start, pos - 1)
        self.quickSort(arr, pos + 1, end)

    def rearrangeArray(self, arr, start, end):
        p1 = start + 1
        p2 = end
        refIndx = random.choice(range(start, end))
        arr[start], arr[refIndx] = arr[refIndx], arr[start]

        while p1 <= p2:
            if arr[p1] <= arr[start]:  # when p1 is at right position
                p1 += 1
            elif arr[p2] >= arr[start]:  # when p2 is at right position
                p2 -= 1
            else:  # when both p1 & p2 are at wrong position, swap them
                arr[p1], arr[p2] = arr[p2], arr[p1]
                p1 += 1
                p2 -= 1

        # Swap arr[start] & arr[p2]
        arr[start], arr[p2] = arr[p2], arr[start]

        return p2  # current position of start
