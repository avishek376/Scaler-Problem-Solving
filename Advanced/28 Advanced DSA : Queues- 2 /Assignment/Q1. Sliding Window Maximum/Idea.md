**Approach:**

1) Have a Dequeue for window length i.e. B.
2) 1st element shall be largest of the window and then after smaller elements of window in decending order.
3) But in the process if smaller element of array is to left of window's larget, it is lost.
4) i.e. we keep 1st element of Dequeue as larget element of window. plx dry run condition of 1st while loop for B elents, this will clear all confusion , if there is.
5) As we move window, in array, windows 1st element is lost if it is there in Dequeue and new element added as per above logic.


       TC: O(N)
       SC: O(N)