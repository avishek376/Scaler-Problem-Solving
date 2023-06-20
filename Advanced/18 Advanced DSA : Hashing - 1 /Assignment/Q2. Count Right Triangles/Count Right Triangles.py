class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        ans=0
        x_hashmap={}
        y_hashmap={}
        for i in A:
            if i in x_hashmap:
                x_hashmap[i] += 1
            else:
                x_hashmap[i] = 1
        for i in B:
            if i in y_hashmap:
                y_hashmap[i] += 1
            else:
                y_hashmap[i] = 1
        for i in range(len(A)):
            x = A[i]
            y = B[i]
            ans += (x_hashmap[x]-1)*(y_hashmap[y]-1)
        return ans
