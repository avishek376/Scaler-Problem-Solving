Essentially you have a start and end pointer starting from the beginning of the string.

You keep moving the end pointer and including more characters until you have all B characters included.

At this point, you start moving start pointer and popping out characters until you still have all the characters of B included. Update your answer and keep repeating the process.

**Approach**
1) stores the frequency of all character in B.
2) We check if the current character represented by end caused a character.
3) to be included which is relevant to B and is still in deficit.
4) move the start pointer popping out the character that
5) still makes sure that all characters in B are covered.
6) check if we have all characters in B covered
  
              
    TC: O(N)
    SC: O(N)