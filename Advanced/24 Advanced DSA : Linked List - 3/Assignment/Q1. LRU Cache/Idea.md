#PROCEUDRE EXPLAINED

        # This code implements an LRU (Least Recently Used) cache,
        # which is a data structure that allows efficient access to a fixed number of recently-used items.
        # The cache has a maximum capacity, and when new items are added and the cache is full,
        # the least recently used item is evicted to make room for the new item.

        # The LRUCache class has two main methods: get and set.

        # The get method takes a key as input and returns the corresponding value
        # if it exists in the cache, otherwise it returns -1.
        # If the key exists in the cache, the corresponding ListNode is removed from its current position in the cache
        # and added to the end of the list, since it is now the most recently used item.

        # The set method takes a key-value pair as input and adds it to the cache.
        # If the key already exists in the cache, its corresponding ListNode is removed from its current position
        # and added to the end of the list. If the cache is full,
        # the least recently used item (which is at the front of the list) is evicted before adding the new item to the cache.
        # The remove and add helper methods are used to update the linked list when ListNodes are added or removed from the cache.


 #NOTE:
        # self.head and self.tail are dummy nodes that are used to make the implementation of the doubly linked list easier.
        # They do not represent actual cache entries, but are used as sentinels to mark the beginning and end of the linked list.

        # self.head.next refers to the first "real" node in the linked list
        # (i.e. the node immediately after the self.head sentinel),
        # while self.tail.prev refers to the last "real" node in the linked list
        #  (i.e. the node immediately before the self.tail sentinel).

        # By using dummy nodes, we can avoid having to check for special cases
        # (such as an empty list or inserting at the beginning or end of the list)
        #  and simplify the implementation of the linked list.      

