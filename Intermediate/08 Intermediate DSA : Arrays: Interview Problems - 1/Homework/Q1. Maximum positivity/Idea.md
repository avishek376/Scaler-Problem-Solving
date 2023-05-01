We can solve this problem using a single while loop:-

For all elements in array :-

1.If ith element is negative, we need to ignore it and go on next element

2. If ith element is non-negative, we will start a second while loop from this position until a negative element arrives.
    a.If size of subarray received using this is greater than size of previous such arrays, then update the answer
    b. else ignore it.

    
    TC: O(N)
    SC: O(1)