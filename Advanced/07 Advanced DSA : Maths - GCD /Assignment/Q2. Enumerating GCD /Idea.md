Any 2 consecutive number is co-prime and their GCD is 1.

So, if A!=B , then their GCD from A -> B id 1

There is no point in converting P and Q to numbers, as they would not fit into a c++ data type, and if it does so (Python), calculating GCD of numbers from a range of 1 to 10100 would take a very very large amount of time.

Instead, the question can be broken down into 2 cases.

Case 1: P == Q
        When P and Q are the same, it is obvious that the greatest divisor is the number itself.

Case 2: P ≠ Q
        When P and Q are not the same, our answer is GCD(P, P+1, P+2, ...., Q)
        But, we know that GCD(P, P+1) is always 1

        Proof:  We know that if a number D divides both A and B, it will also divide abs(A-B)
                Now, if B = A+1, let's assume D to be a number that divides both A and B.
                D should also divide abs(A-B) = abs(A - (A+1)) = 1
                But the only number to perfectly divide 1 is 1 itself. Hence D has to be 1.

        Therefore, if P ≠ Q, the answer is 1.


        TC: O(1)
        SC: O(1)