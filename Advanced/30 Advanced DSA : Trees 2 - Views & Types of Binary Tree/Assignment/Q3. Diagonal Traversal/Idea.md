Method 1:
The idea is to use map. We use different slope distances and use them as key in map. Value in map is vector (or dynamic array) of nodes. We traverse the tree to store values in map. Once map is built, we print contents of it.

Suppose slope at current node is x then:
a) The slope of it’s right child remains same i.e x
b) The slope of it’s left child becomes x + 1

As the order in the output matters so we have to move in the pre-order traversal format in the tree A i.e
1)Process the root push root to map[slope(root)].push(root)
2)Go to left child
3)Go to right child
Keep repeating the above steps until the whole tree is traversed.

    TC : O(N)
    SC: O(H), H is height of Tree

Method 2: Using Queue

1) Every node will help to generate the next diagonal. We will push the element in the queue only when its left is available. 

2) We will process the node and move to its right.


    TC: O(N), because we are visiting nodes once.
    SC: O(H), H is height of Tree, because we are using queue.