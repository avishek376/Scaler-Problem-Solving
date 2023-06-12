class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        #result array for returnning
        result = []
        def TOH(n, source, temp, destination):
            if n == 0:
                return
            # Move n-1 discs from source to helper step by step
            TOH(n-1, source, destination, temp)
            # Move n discs from source to destination
            current = [n, source, destination]
            result.append(current)
            #Move n-1 discs from helper to destination
            TOH(n-1, temp, source, destination)

        TOH(A, 1, 2, 3)

        return result
