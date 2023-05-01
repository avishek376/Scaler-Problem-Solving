**Moore's Voting Algo:**

If we delete 2 distinct elements majority won't change.
loop through each element & maintain a frequency/ count of the
element that has potential of being the majority element.

If the next ele. is same increase the count/freq else
decrease it.
If the count reaches 0 then by the potential ele. increament/ reset it to 0.


******
If we cancel out each occurrence of an element X with all the other elements that are different from X, then X will exist till the end if it is a majority element.
Loop through each element and maintain a count of the element that has the potential of being the majority element.

If the next element is the same, then increments the count, otherwise decrements the count.
If the count reaches 0, then update the potential index to the current element and reset the count to 1.

    
    TC: O(N)
    SC: O(1)