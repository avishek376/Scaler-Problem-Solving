Idea - 1
Loop through the character array and use the ascii codes of each character to convert them to lowercase.
If A[i] is uppercase, we can change it to ‘a’ + (A[i]-‘A’)

TC: O(N)
SC: O(1)