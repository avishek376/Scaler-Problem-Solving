Using seive, we can store the smallest prime factor for all the numbers upto the maximum no (here it is 106).
This above information helps in determining the prime factors for any no in O(log n) time-complexity for each query.

We take each no in the input array. Then prime factorise it to count the powers of each prime factors in a number.
    
    N = (p1n1) * (p2n2) * (p3n3).
    
    Here, N can be represented as p1 prime raised to the power n1 muliply p2 prime raised to n2 multiply p3 raised to n3.
    
    So, total factors of N will be (n1 + 1) * (n2 + 1) * (n3 + 1).
    
    For eg: 18 = (21) * (32).

So, total factors = 2*3 = 6.

    TC: O(NloglogN)+O(log(max ))
    SC: O(N)