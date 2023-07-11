**Approach**

A simple approach is to use the recursive implementation of the recursive relation given.

For ex: Calculate 4th term.
    
                   fib(4)   
                 /        \     
             fib(3)      fib(2)
            /    \       /    \     
      fib(2)   fib(1)  fib(1) fib(0)
      /     \
    fib(1) fib(0)
We can see that the 2nd term is calculated multiple times.

If we try to find large Fibonacci numbers, there will be more and more repetitions that are bad.

Time complexity of above: O(2^N) is exponential.

To avoid this, try to store the term which is calculated once and before calculating any other term check if it is already calculated or not.

Use DP in this case

If we already have that term use that. This will save us a lot of repetitions.

In this we are only calculating each term once, So, time complexity will be linear.

    TC: O(N)
    SC: O(N)