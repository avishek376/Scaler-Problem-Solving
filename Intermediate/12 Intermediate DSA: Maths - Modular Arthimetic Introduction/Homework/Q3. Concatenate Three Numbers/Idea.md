Approach 1:

The minimum number will always be formed if the smallest number is taken first, the second smallest is taken second, and the largest is taken last.

This will be true only if the numbers have the same length.

So, you can also sort the numbers and concatenate them to get the answer.
        
    TC: O(NlogN)
    SC: O(1)


Approach 2:

To get the minimum number the minimum digit among a,b & c will be min(a,b,c)
like that max will be max(a,b,c)
middle one will be a+b+c-min-max
    
    TC: O(1)
    SC: O(1)
