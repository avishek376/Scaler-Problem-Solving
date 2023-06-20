As mentioned in the hint, run two loops by fixing the two diagonally opposite rectangle ends.

We have fixed the one diagonal of the rectangle and two corner points.

From this, we can easily find the other two rectangle points.

Suppose we have two diagonally opposite points: (x1, y1) and (x2, y2). Then the other two points of the rectangle must be (x1, y2) and (x2, y1).

We have to check if these two points (x1, y2) and (x2, y1) are given or not.

If present, increment the answer.
We have incremented the answer twice for every rectangle because every rectangle has two diagonals.

So, our final answer will be half of the answer obtained after running two loops.

    
    TC: O(N)
    SC: O(N)