class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxEle = max(A)
        count = 0
        for i in A:
            if i == maxEle:
                pass
            else:
                count += 1
        return count

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_value = 0
        max_count = 0
        for x in A:
            if x == max_value:
                max_count += 1
            elif x > max_value:
                max_count = 1
                max_value = x
        return len(A) - max_count

        TC: O(N)
        SC: O(1)

    class Solution:
        # @param A : list of integers
        # @return an integer
        def solve(self, A):
            count=0
            A.sort()
            mx = A[-1]
            #print(mx,A)
            for i in range(0,len(A)):
                if A[i] == mx:
                    count+=1
            return len(A)-count
            
            TC: O(NlogN)
            SC: O(1)
'''