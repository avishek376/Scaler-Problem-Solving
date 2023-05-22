Observations:
When
A = 1 -> 0
A = 2 ->01
A = 3 ->0110

As we can see that there are two part in string (when A>=2)
first part is repeating of (A-1)th> step and second part is also compliment of (A-1)th step

for A = 3 -> first part - 01 ( it is same as when A == 2) second part- 10 ( compliment of when A == 2)

We know that on every expansion, the length of String is 2(A-1)

so what we can do when B value is <= mid we can search the result in first part of (A-1)th step solve(A-1, B)

and when B > mid we can search the result in (A-1)th step but compliment of that index to get the actual index in 1st part we have to do B - mid.


1) Base cond.n. in every row where index=0, return value = 0
2) `ans(A-1,B//2) `   # this will go to value and coordinate of parent element
3) If the kid is at left index or even index, it will be same as parent element
4) Otherwise, if kid is at right or odd index, it will have complimentary value

    
    TC :O(log2 B)
    SC :O(log2 B)