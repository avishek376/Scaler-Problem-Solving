from collections import defaultdict
from collections import Counter


class Solution:
    # @param A : list of list of integers
    # @return a list of integers

    freq = Counter()  # to store frequence of an element in the stack.
    stacks = defaultdict(list)  # to maintain the structure of stack and pop out top most element in case of a tie
    max_freq = 0

    def solve(self, A):
        self.freq = Counter()
        self.stacks = defaultdict(list)
        self.max_freq = 0
        ans = []
        for i in range(0, len(A)):
            if (A[i][0] == 1):
                self.push(A[i][1])
                ans.append(-1)
            else:
                x = self.pop()
                ans.append(x)
        return ans

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.max_freq:
            self.max_freq = f
        self.stacks[f].append(x)

    def pop(self):
        x = self.stacks[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return x


'''class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        freqMap = {}    #for maintaining the frequency of each ele.
        occurMap = {}   #for maintaining the occurances of each ele. by ele,stack in hashmap
        resList = []    #ans list to maintain
        
        maxFreq = -10**8    #var for check maximum frequency
        for i in A:
            if i[0]==1: #operation push
                val = i[1]
                if val not in freqMap:  #maintaining the freq in the freqMap
                    freqMap[val] = 1
                else:
                    freqMap[val] += 1
            
                if freqMap[val] in occurMap:    #maintaining the occurance in the main map
                    occurMap[freqMap[val]].append(val) #if the freqMap ele is present then by that val enter the ele into the stack
                else:
                    occurMap[freqMap[val]] = [val]  #if not present then create a stack
                resList.append(-1)

                maxFreq = max(maxFreq, freqMap[val])
            else:                              #operation pop
                
                ele = occurMap[maxFreq].pop() #taking the maxFreq and poping the val from main map
                freqMap[ele] -= 1 #decreasing the freqMap val as well
                resList.append(ele)
                if len(occurMap[maxFreq]) == 0: #if len of occurance map's stack is 0 decrease it by 1
                    maxFreq-=1
        return resList'''