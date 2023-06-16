class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        def painterCount(arr, m):
            time = 0
            workerCount = 1
            for i in range(len(arr)):
                time += arr[i]
                if time > mid:
                    time = arr[i]
                    workerCount += 1
            return workerCount

        mod = 10000003
        l = max(C)
        summ = 0
        for i in range(len(C)):
            summ += C[i]
        h = summ
        while (l <= h):
            mid = l + (h - l) // 2
            if painterCount(C, mid) <= A:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return (ans * B) % mod
