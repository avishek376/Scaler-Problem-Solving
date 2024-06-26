class Solution:
    # @param A : list of integers
    # @return a list of integers

    class Solution:
        # @param A : list of integers
        # @return a list of integers
        def solve(self, A):
            maxv = max(A)
            countArr = [0] * (maxv + 1)

            for i in range(len(A)):
                countArr[A[i]] += 1

            ans = []
            for i in range(maxv + 1):
                ans += countArr[i] * [i]

            return ans
    '''
    def solve(self, A):
                                      # for this I used an index array upto max element of A not 10**5 to save time
        max1=float("-inf")
        for i in A:
            if i >max1:
                max1=i

        index=[0]*(max1+1)           # created an index array starting from 0 upto max element as end
        for i in A:
            index[i]+=1              # here whatever be element of A its index  will get its total count\

        ans=[]
        for i in range(max1+1):       # picks element one by one
            ans+=index[i]*[i]         # in ans array the value of index * single elemnt array =[el,el,el,...(upto its value in index)]
        return ans
        
        '''


'''class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        mx = max(A)
        freq = [0 for j in range(mx + 1)]
        for x in A:
            freq[x] += 1
        ans = []
        for i in range(mx + 1):
            for j in range(freq[i]):
                ans.append(i)
        return ans'''