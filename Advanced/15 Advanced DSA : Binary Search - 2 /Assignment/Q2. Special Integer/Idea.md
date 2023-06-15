You need to find the maximal K.
Think of a way to do this by binary search.
You can use binary seacrh to find if a certain K is allowed or not.
if it is, you try finding a bigger answer
if not, try finding a smaller answer.

int l = 1, r = a.length;
        while(l <= r) {
            int m = (l + r) >> 1;
            if(check(a, b, m))    l = m + 1;
            else        r = m - 1;
        }
        return l-1;
How do we check for a particular K if it is allowed or not?

We can use the sliding window technique.
First we can compute the sum from 0 to k-1. Check if it is less than of equal to B or not.
To move to the next window we can simply subtract a[0] from the sum and add a[K], and repeat the process.


    TC: O(NlogN)
    SC: O(1)