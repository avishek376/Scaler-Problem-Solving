**Approach**

The pseudocode would look something like this:

1) Create a new empty stack st

2) Iterate over array `A`,
   where `i` goes from n-1 to 0 index.
    a) We are looking for value just smaller than `A[i]`. So keep popping from `st` till elements in `st.top() >= A[i]` or st becomes empty.
    b) If `st` is non-empty, then the top element is our previous element. Else the previous element does not exist. 
    c) push `A[i]` onto st
    
    
    TC: O(N)
    SC: O(N)