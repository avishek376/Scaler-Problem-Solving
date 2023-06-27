This question depends on your data structure knowledge as you can quickly solve this question using a suitable data structure which is the stack in our question.
You have two types of instructions in this question:

So you can easily push the new id in the stack to keep track of the latest player
who has the ball.
Now, you should pass the ball to the previous player who forwarded you the ball, so you can easily pop the last player from the stack.
   
    TC: O(N)
    SC: O(N)