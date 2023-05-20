class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        i = j = 0
        list = []
        sum = A[0]
        flag = False

        while j < n and i < n:
            if sum == B:
                # current window sum = B
                flag = True
                break

            elif sum < B:
                # current window sum < B
                if j + 1 == n:
                    break
                j = j + 1
                sum = sum + A[j]

            else:
                # current window sum > B
                if i + 1 == n:
                    break
                i = i + 1
                sum = sum - A[i - 1]

        if flag == False:
            return [-1]

        for k in range(i, j + 1):
            list.append(A[k])

        return list
#   TC:O(N)/SC:O(1)

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n  = len(A)
    
        currSum = 0
        
        dict1 = {}
        for i in range(n):
            currSum += A[i]
                
            if currSum == B:
                return A[:i+1]
            if currSum-B in dict1:
                return A[(dict1[currSum - B] + 1):i+1]
            dict1[currSum] = i
            
        # return [-1]     /TC:O(N)/SC:O(N)
'''