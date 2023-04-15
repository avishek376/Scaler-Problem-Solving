from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def cmp_func(x, y):
            # Sorted by value of concatenated string increasingly
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        # Build nums contains all numbers in the String format.
        A = [str(num) for num in A]

        # Sort nums by cmp_func decreasingly.
        A.sort(key=cmp_to_key(cmp_func), reverse=True)

        # Remove leading 0s, if empty return '0'.
        return ''.join(A).lstrip('0') or '0'
