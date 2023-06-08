This problem is very simple if you know Fermat’s Little Theorem.

The basic approach to solve this problem is to find factorial of B by taking mod with (P-1), where P is a prime. In this problem, 10007 is also a prime.

After calculating the factorial of B, you can calculate A ^ B! by simply taking mod with P.


    TC: O(B + logM)
    SC: O(1)