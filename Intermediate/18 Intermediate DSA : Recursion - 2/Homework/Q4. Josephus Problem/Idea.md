After the first person (B-th from the beginning) is killed, 
A-1 persons are left. So we call Josephus(A – 1, B) to get the 
position with A-1 persons. But the position returned by 
Josephus(A – 1, B) will consider the position starting from B%A + 1. 
So, we must make adjustments to the position returned by Josephus(A – 1, B). 
    
    TC : O(A) / O(N)
    SC : O(A) / O(N)