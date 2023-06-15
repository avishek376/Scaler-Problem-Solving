Say L = lcm(B, C), the least common multiple of B and C, and let f(x) be the number of magical numbers less than or equal to x.

A well known result says that L = (B*C)/gcd(B,C), and that we can calculate the function gcd.
Then f(x) = x/B + x/C - x/L (floor of all the divisions)

Why?

    There are x/B numbers B, 2B, 3B.... that are divisible by B,
    There are x/C numbers C, 2C, 3C.... that are divisible by C,
    We need to subtract the x/L numbers divisible by B and C that we double-counted.

Finally,the answer must be between 0 and A * min(B,C).

If x increases f(x) increases, we can use Binary Search on x to find the Ath number.

Algorithm:
    
    low=1 and high = A * min(B,C)
    while low <= high
    Find mid = (low + high)/2
    Find f(mid) let it be count
    If count>=A then mark it as a answer and try to find smaller number which implies high = mid-1
    Else low = mid+1

    TC: O(log (A * min(B, C))) 
    SC: O(1).