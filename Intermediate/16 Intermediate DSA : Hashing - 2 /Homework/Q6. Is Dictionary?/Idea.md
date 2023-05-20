Let’s check whether all adjacent words a and b have a <= b.

To check whether a <= b for two adjacent words, a and b, we can find their first difference.
For example, “applying” and “apples” have the first difference of y and e.
After, we compare these characters to the index in order.

Care must be taken to deal with the blank character effectively.
If, for example, we are comparing “app” to “apply”, the first difference is between (null) and “l”.

    
    TC: O(N)
    SC: O(N)