class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        n = len(A)

        count = 0
        lst = []
        for i in range(n):
            lst.append(A[i])

        for i in range(n - 1):
            if count < B:
                minEle = lst[i]
                minIndex = i
                for j in range(i + 1, n):
                    if lst[j] < minEle:
                        minEle = lst[j]
                        minIndex = j
                lst[i], lst[minIndex] = lst[minIndex], lst[i]
                count += 1
            else:

                break
        return lst[B - 1]


'''class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        a = []
        for x in A:
            a.append(x)
        for i in range(0, B):
            # finding the minimum element from the remaining array
            min_idx = i
            for j in range(i + 1, len(a)):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return a[B - 1]'''