Each character must come in multiples of A if we are to represent the string as a concatenation of A strings.
Why?

Because that count divided by A will the number of times that particular character appears in 1 string.

So we maintain a hash which stores the frequency of each character.

Then we iterate over the hash and check if each character that appeared in the array appeared as a mutiple of A or not.
If there exists even 1 character whose hash[i] % A is not equal to 0, it implies we cannot represent the string as A concatenated strings
Else the answer is yes.

    TC: O(N)
    SC: O(N)