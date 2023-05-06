from functools import cmp_to_key


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):

        def colorSort(a, b):

            if a > b:
                return 1
            elif a == b:
                return 0
            elif a < b:
                return -1

        A.sort(key=cmp_to_key(colorSort))
        return A
