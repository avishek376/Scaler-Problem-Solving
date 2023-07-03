**Method 1 – Using Queue**

The following are steps to print Bottom View of Binary Tree.

1.We put tree nodes in a queue for the level order traversal.

2.Start with the horizontal distance(hd) 0 of the root node, keep on adding left child to queue along with the horizontal distance as hd-1 and right child as hd+1.

3.Also, use a TreeMap which stores key value pair sorted on key.

4.Every time, we encounter a new horizontal distance or an existing horizontal distance put the node data for the horizontal distance as key. For the first time it will add to the map, next time it will replace the value. This will make sure that the bottom most element for that horizontal distance is present in the map and if you see the tree from beneath that you will see that element.

Time Complexity of hashing based solution can be considered as O(n) under the assumption that we have good hashing function that allows insertion and retrieval operations in O(1) time.
In the above C++ implementation, map of STL is used. map in STL is typically implemented using a Self-Balancing Binary Search Tree where all operations take O(Logn) time.
Therefore time complexity of the above implementation is O(nLogn).


**Method 2- Using HashMap()**

**Approach:**

1) Create a map like, map where key is the horizontal distance and value is a pair(a, b) where a is the value of the node and b is the height of the node. 

2) Perform a pre-order traversal of the tree.

3) If the current node at a horizontal distance of h is the first we’ve seen, insert it in the map.

4) Otherwise, compare the node with the existing one in map and if the height of the new node is greater, update in the Map.


    TC: O(N)
    SC: O(N)