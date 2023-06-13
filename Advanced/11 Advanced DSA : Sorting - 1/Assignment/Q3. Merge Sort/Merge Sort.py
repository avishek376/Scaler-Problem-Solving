class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        self.mergeSort(A, 0, n - 1)
        return A

    def mergeSort(self, arr, start, end):
        if start == end:
            return

        midElement = (start + end) // 2

        self.mergeSort(arr, start, midElement)  # Left array
        self.mergeSort(arr, midElement + 1, end)  # Right array
        self.mergeSubarrays(arr, start, midElement, end)  # Merge left and right sorted array

        return arr

    def mergeSubarrays(self, arr, start, midElement, end):
        # consider two sorted sub arrays
        ##1 start to midElement
        ##2 midElement+1 to end
        p1 = start
        p2 = midElement + 1
        p3 = 0

        tempArray = [0] * (end - start + 1)

        while (p1 <= midElement and p2 <= end):
            if arr[p1] < arr[p2]:
                tempArray[p3] = arr[p1]
                p1 += 1
                p3 += 1
            else:
                tempArray[p3] = arr[p2]
                p2 += 1
                p3 += 1

        # Copying remaining elements
        while p1 <= midElement:
            tempArray[p3] = arr[p1]
            p1 += 1
            p3 += 1

        # Copying remaining elements
        while p2 <= end:
            tempArray[p3] = arr[p2]
            p2 += 1
            p3 += 1

        # copying the sorted tempArray (merged two sub arrays) to main array
        i = start
        j = 0

        while i <= end:
            arr[i] = tempArray[j]
            i += 1
            j += 1
