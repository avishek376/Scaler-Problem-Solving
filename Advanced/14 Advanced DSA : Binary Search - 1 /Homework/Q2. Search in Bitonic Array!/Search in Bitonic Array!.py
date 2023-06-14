class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        pivot = 0
        # if pivot is
        '''
        /
       /
       or
       \
        \
        '''
        if A[n - 1] > A[n - 2]:
            pivot = n - 1
        elif A[0] > A[1]:
            pivot = 0

        s = 1
        e = n - 2

        # search the pivot ele. first
        '''
         /\
        /  \
        
        '''
        while s <= e:
            mid = e + (s - e) // 2
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                pivot = mid
                break
            elif A[mid] > A[mid - 1]:
                s = mid + 1
            else:
                e = mid - 1

        # now from left to check upto pivot point
        s, e = 0, pivot
        while s <= e:
            mid = e + (s - e) // 2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                e = mid - 1
            else:
                s = mid + 1

        # now from pivot to check upto right or end pointer
        s = pivot + 1
        e = n - 1
        while s <= e:
            mid = e + (s - e) // 2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                s = mid + 1
            else:
                e = mid - 1
        return -1
