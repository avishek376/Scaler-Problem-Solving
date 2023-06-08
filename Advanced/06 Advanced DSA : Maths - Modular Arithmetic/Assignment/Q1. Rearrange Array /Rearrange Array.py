class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        N = len(A)

        for i in range(N):
            A[i] = A[i] * N

        for i in range(N):
            newIndex = A[i] // N
            newVal = A[newIndex] // N
            A[i] += newVal

        for i in range(N):
            A[i] = A[i] % N

        return A
