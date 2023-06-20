It is one of the easiest problems in this section.
You just need to simulate what has been stated in the problem.

Iterate over all the consecutive sequence of digits of the number and store the product in a set using hashing.
If the product is already present in the set at any point then the number is not Colorful.
Otherwise, it is a Colorful number.

Example:

A = 123
1 2 3 12 23 123
1 -> 1
2 -> 2
3 -> 3
12 -> 2  we have already encountered 2 before. Return 0

**Observations**:-

1) Create all the contiguous - sequence like 

3245

3   32  324   3245

2   24  245

4   45

5

2) Now we will generate each and every sequence product.
3) To avoid duplicate we are inserted all those products to set.
4) If any duplicacy occurs then return 0 else 1
    
    TC: O(N^2)
    SC: O(N)
