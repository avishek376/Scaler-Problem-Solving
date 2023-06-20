**Observations**:
1) add all the elements in set,by that duplicates will be deducted.
2) Iterate to every ele. in array and take its previous ele
3) Check it's previous ele is present or not in the set.
4) If present then it's not a valid starting point for creating the sequence.
5) If not then the current ele is the valid starting point to start with.
6) Increment the counter and take maximum length out of it.


    TC: O(N)
    SC: O(N)