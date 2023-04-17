An Efficient Solution is to solve the above problem in O(n) time and O(1) extra space. The idea is to use sliding window of size k. Keep track of sum of current k elements. To compute sum of current window, remove first element of previous window and add current element (last element of current window).


```
   1) Initialize res_index = 0 // Beginning of result index
   2) Find sum of first k elements. Let this sum be 'curr_sum'
   3) Initialize min_sum = sum
   4) Iterate from (k+1)'th to n'th element, do following
      for every element arr[i]
         a) curr_sum = curr_sum + arr[i] - arr[i-k]
         b) If curr_sum < min_sum
              res_index = (i-k+1)
   5) Print res_index and res_index+k-1 as beginning and ending
      indexes of resultant subarray.```

TC: O(N)
SC: O(1)