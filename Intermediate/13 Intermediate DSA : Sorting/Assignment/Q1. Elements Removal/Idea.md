Let’s find the count of how many times an element will contribute to the answer.

Remove any element from the array. The cost of this operation is equal to the sum of array elements irrespective of which element gets removed.

If we remove another element from the array, the cost of this operation will be ( cost of the previous operation - the element which gets removed in the last operation.)

So, we can easily observe that it is wise to remove the highest element first to make the total cost minimum, and elements also follow a pattern.

So, [a,b,c,d] the process will following below steps:

    removal                          cost

        a                           a+b+c+d
        b                            b+c+d
        c                             c+d
        d                              d

    here, total cost = a+2b+3c+4d
To make this total cost minimum 'a' should be max & 'd' should be minimium.

    TC: O(NlogN)
    SC: O(1)