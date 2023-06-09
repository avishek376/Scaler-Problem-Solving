Let’s consider if there were only 2 people with strength A and B (A<=B). then A would attack B, leading to A, B-A.
It would continue until it gets smaller than A or A, B%A. Then the process would repeat as A%(B%A), B%A, and so on…

You can see this is exactly what is done in Euclid GCD algorithm. So, the answer is always gcd of numbers.

    TC: O(Nlog(max of ele.))
    SC: O(logN)