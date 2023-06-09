We can’t loop, so we can try for another approach, i.e., find the lcm(least common multiple) of B and C and find the number of
elements less than equal to A, which is divisible by lcm.
lcm(A,B)=(A*B)/(gcd(A,B))


    TC: (logN)
    SC: O(1)