First, we will find the number of elements that are less than or equal to B. Let the count comes out to be X.

We know that we need at most X-1 swaps to make all X elements to be consecutive.
Maintain a window of X and check how many elements we need to swap so that all X elements come in that window.

We store the minimum of all that and return that.

    
    TC: O(N)
    SC: O(1)