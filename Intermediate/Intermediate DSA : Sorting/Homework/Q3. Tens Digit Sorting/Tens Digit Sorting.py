from functools import cmp_to_key


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        def compa(a, b):
            ta = (a // 10) % 10
            tb = (b // 10) % 10

            if ta < tb:
                return -1
            if a > b and ta == tb:
                return -1

            else:
                return 1

        A.sort(key=cmp_to_key(compa))

        return A
