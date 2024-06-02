class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        n = len(A)
        S = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        for i in range(n - 1, -1, -1):
            if A[i] in S:
                count += n - i
        return count % 10003


'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        mySet = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        i = len(A)-1
        count = 0
        result = 0
        while i>=0:
            if A[i] in mySet:
                count+=1
                result += count
            else:
                count+=1
            i-=1
        return result%10003
        
        TC: O(N)
        SC: O(1)
'''

