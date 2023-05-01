The most basic brute force approach would be to find the sum of every subarray and check if it less than B,
we will put it in a variable which will store the maximum value less than B.
The time complexity of this approach would be O(N ^ 3).

But, for the given constraints, the best we can do is O(N ^ 2).
We can do this easily just by modifying the way we iterate through the loop.

We will use the following pseudocode:

    ans = 0
    for(start = 0, start < size; start += 1)
        sum = 0
        for(end = start; end < size; end += 1)
            sum += array[end]
            if(sum <= MaximumValue)
                ans = max(sum, ans)
            else
                break

Using this, we are checking the sum of every subarray but this method is faster.

Refer to the complete solution for more details.
