What if you maintained the current minimum in a variable and only stored the places where the minimum changes or the element is the same as the minimum.

pop() becomes a little trickier in such a case.
You only pop() from the min stack if the top() of the min stack is the same as the current minimum.

    TC: O(N)
    Space complexity: O(N + X) where X = number of places where minimum changes or the element is the same as the minimum.