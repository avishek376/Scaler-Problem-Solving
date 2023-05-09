Consider that any valid arithmetic progression will be in sorted order.

    **Idea is while sorting in ascending order comparator function 
        returns -1 when a < b
                0  when a == b
                1  when a > b**

Sort the array, then check if the differences of all consecutive elements are equal.

    TC: O(NlogN)
    SC: O(1)