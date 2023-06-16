You are already halfway there if you have already solved the problem corresponding to hint1.

You can do a binary search for the answer :

  start = 0, end = max_time_possible
  mid = (start + end) / 2
  if isPossible(mid): 
      end = mid - 1
  else 
    start = mid + 1
Now, let us look into how isPossible would be implemented.

Keep assigning boards to painter greedily till the time taken < mid,
if you run out of painters, isPossible = false.
else isPossible = true.

    TC: O(NlogN)
    SC: O(1)