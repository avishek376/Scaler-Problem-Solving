If we are required to do K left rotations, we can append the first K elements of the array to the back and delete and delete them from the front

If K is greater than the size of the array, we can simply perform modulo on it with array size as after exact rotation of array’s size times the array return to its original state

    TC: O(N)
    SC: O(1)