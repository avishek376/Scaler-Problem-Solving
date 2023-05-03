We can choose any X. So lets try to choose optimally. Say for any ith bit in binary values of A and B, the bit is set for both A and B.
Then we can also set it in X such that XOR with both becomes 0.
Similarly, if for both A and B the bit was unset, we unset it for X as well. XOR of that bit remains 0.
Now try to think if the bit is set for one and unset for other what will X and our result be.

That's right doesnt matter if the bit is set or unset that bit will be added to our answer as either A ^ X != 0 or B ^ X != 0 for that bit.
Now did you take the observation? If we are adding a bit to out answer if that bit is set for one number and unset for another,
then it is A ^ B operation itself. So A ^ B is our answer.

    TC: O(1)
    SC: O(1)