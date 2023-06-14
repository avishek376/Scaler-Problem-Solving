Using the Binary Search algorithm to find the index.

Start with two pointers, one pointing to the beginning of the array (low) and the other pointing to the end of the array (high).

While the low pointer is less than or equal to the high pointer, do the following:

Find the middle element of the array by calculating the average of low and high. Let’s call it mid.

Compare the target value (B) with the element at the mid index in the array (A[mid]):

    If A[mid] == B, it means we have found the target value. Return the value of mid as the index of the target value.
    
    If A[mid] < B, it means the target value should be in the right half of the array. Update the low pointer to mid + 1 and continue searching in the right half.
    
    If A[mid] > B, it means the target value should be in the left half of the array. Update the high pointer to mid - 1 and continue searching in the left half.


As the value is k <= target_value, actually we are finding floor of a target number over here.

So, while discarding the right hand-side we will keep the answer = mid as our potential answer 
and keep traversing.

    TC: O(log N)
    SC: O(1)
