V : 
1 |  2  |  3  | 4
2 |  3  |  4  | 5

Lets first try to reduce it into a simpler problem. 
We know that within a column, we can choose at max 1 element. 
And choosing either of those elements is going to rule out choosing anything from the previous or next column. 
This means that choosing V[0][i] or V[1][i] has identical bearing on the elements which are ruled out. 
So, instead we replace each column with a single element which is the max of V[0][i], V[1][i].

Now we have the list as : 
2 3 4 5

Here we can see that we have reduced our problem into another simpler problem.
Now we want to find maximum sum of values where no 2 values are adjacent. 
Now our recurrence relation will depend only on position i and,
 a "include_current_element" which will denote whether we picked last element or not.

MAX_SUM(pos, include_current_element) = 
IF include_current_element = FALSE THEN   
    max ( MAX_SUM(pos - 1, FALSE) , MAX_SUM(pos - 1, TRUE) )

ELSE
    MAX_SUM(pos - 1, FALSE) + val(pos) 


    
    TC: O(N*M)
    SC: O(N*M)