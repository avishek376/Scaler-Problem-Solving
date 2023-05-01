Create a prefix array pref[] where pref[i+1] will store the sum of numbers with even indices in the subarray A[0…i]. 
Now, the sum of numbers with even indices in the range [L, R] can be easily calculated in O(1) as pref[R + 1] – pref[L].
    
    TC: O(N + Q)
    SC : O(N + Q)