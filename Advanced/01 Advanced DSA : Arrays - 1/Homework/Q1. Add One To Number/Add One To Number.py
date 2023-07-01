class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        res = []
        strng = ''.join([str(i) for i in A])

        temp = str(int(strng) + 1)
        for i in temp:
            res.append(int(i))
        return res


# IF THERE IS NO LEADING ZERO IN ARRAY THEN THIS BELOW SOLUTION WILL WORK
'''class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)

        for i in range(n-1, -1, -1):
            if A[i]<9:
                A[i]+=1
                return A
            else:
                A[i]= 0

        return [1] + A'''

# APPROACH-2
'''class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A[-1] += 1
        temp = 0
        tempSum = 0
        # traversing the digits of the number in reverse order
        for i in range(len(A) - 1, -1, -1):
    	    tempSum = A[i] + temp
    	    temp = (A[i] + temp) // 10
    	    A[i] = tempSum % 10
        if temp > 0:
    	    A = [temp] + A
        i = 0
        while i < len(A):
            if A[i] > 0:
                break
            i += 1
        return A[i:]'''