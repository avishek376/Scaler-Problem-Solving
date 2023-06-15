Let us say S is the answer. We know that 0 <= S <= A.

Consider any random number r.
If r*r <= A, S >= r , i.e. S would lie towards right of r
If r*r > A, S < r, i.e. S would lie towards left of r

Run a Binary Search Algorithm, by using the above Fact.

    Set the lower bound low as 0 and the upper bound high as A.
    While low <= high, perform the following steps:
    a. Calculate the midpoint mid as the average of low and high.
    b. Compare mid squared with A:
    If mid * mid is equal to A, return mid as the square root.
    If mid * mid is less than A, update low to mid + 1.
    If mid * mid is greater than A, update high to mid - 1.


After the binary search ends, return the value of high as the floor value of the square root of A.

    TC: O(log(N))
    SC: O(1)