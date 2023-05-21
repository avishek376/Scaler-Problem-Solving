Use recursion to apply the formula. Do not forget to add base cases or else you might run into an infinite loop.

We can observe that this implementation does a lot of repeated work (see the following recursion tree). So this is a bad implementation for nth Fibonacci number.

                       fib(5)   
                     /                \
               fib(4)                fib(3)   
             /        \              /       \ 
         fib(3)      fib(2)         fib(2)   fib(1)
        /    \       /    \        /      \
      fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
      /     \
    fib(1) fib(0)


    TC : O(n) = T(n-1) + T(n-2) which is exponential.
    SC : O(n) if we consider the function call stack size, otherwise O(1).