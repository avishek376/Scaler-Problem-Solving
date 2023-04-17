**Moore's Voting Algo**

It is important to note that if at a given time, you have 3 distinct element from the array, if you remove them from the array, your answer does not change.

Assume that we maintain 2 elements’ counts as we traverse along the array.

When we encounter a new element, there are 3 cases possible :

We don’t have 2 elements yet. So add this to the list with count as 1.

This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now. Removing them does not change the answer. So decrement 1 from count of 2 existing elements. If their count falls to 0, obviously its not a part of 2 elements anymore.

The new element is same as one of the 2 elements. Increment the count of that element.

Consequently, the answer will be one of the 2 elements left behind. If they are not the answer, there is no element with count > N / 3.

TC: O(N)
SC: O(1)