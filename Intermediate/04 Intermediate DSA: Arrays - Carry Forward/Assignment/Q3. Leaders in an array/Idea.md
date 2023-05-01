Note that for an element to be greater than all the elements towards its right , it just needs to be greater than the maximum element towards its right.
Keep a variable ‘mx’ which stores the maximum till now and initialize it with the last element of the array and also add the last element to our answer array. Iterate from n-2 to 0 , at every index we check if that number is greater than the variable mx. If it is we add the element to our answer array and change mx to that variable.

    TC: O(N)
    SC: O(1)