If you are still stuck at reversing the full linked list problem,
then would maintaining curNode, nextNode and a tmpNode help?

Maybe at every step, you do something like this :

    tmp = nextNode->next;
            nextNode->next = cur;
            cur = nextNode;
            nextNode = tmp;
Now, let’s say you did solve the problem of reversing the linked list and are stuck at applying it to the current problem.
What if your function reverses the linked list and returns the endNode of the list.
You can simply do
prevNodeOfFirstNode->next = everseLinkedList(curNode, n - m + 1);

Explanation in the video:
We can also find the two pointers between which the list needs to be reversed and only reverse that portion.
We will also have to make two new connections, one from the node just before the first node in the original portion to the node at the starting of the reversed portion, another from the first node of the original portion to the node after the last node in the original portion.
A detailed explanation is in the video.

    TC: O(N)
    SC: O(1)