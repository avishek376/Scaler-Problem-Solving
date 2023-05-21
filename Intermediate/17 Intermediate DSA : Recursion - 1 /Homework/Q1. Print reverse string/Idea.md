To reverse the string, we have to implement the LIFO nature of stack with recursion.
Take the current character, and recursively solve the problem for then remaining portion of the string.
The base case is when the entire string has been traversed.
    
    TC :O(N)
    SC :O(N)