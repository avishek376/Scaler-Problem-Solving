class ListNode:
    def __init__(self, key, value):
        self.key = key  # the key for the cache entry
        self.value = value  # the value for the cache entry
        self.prev = None  # a reference to the previous ListNode in the linked list
        self.next = None  # a reference to the next ListNode in the linked list


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity  # the maximum number of items the cache can hold
        self.cache = {}  # a dictionary to store the cache entries, with keys mapping to ListNodes
        self.head = ListNode(-1, -1)  # a dummy ListNode at the front of the linked list
        self.tail = ListNode(-1, -1)  # a dummy ListNode at the end of the linked list
        self.head.next = self.tail  # link the head to the tail
        self.tail.prev = self.head  # link the tail to the head

    # @return an integer
    def get(self, key):
        if key in self.cache:  # if the key is in the cache
            node = self.cache[key]  # get the ListNode associated with the key
            self.remove(node)  # remove the ListNode from its current position
            self.add(node)  # add the ListNode to the end of the linked list (since it is now the most recently used)
            return node.value  # return the value associated with the key
        return -1  # if the key is not in the cache, return -1

    # get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:  # if the key is already in the cache
            self.remove(self.cache[key])  # remove the ListNode associated with the key from its current position

        node = ListNode(key, value)  # create a new ListNode for the new cache entry
        self.cache[key] = node  # add the ListNode to the cache dictionary
        self.add(node)  # add the new ListNode to the end of the linked list

        if len(self.cache) > self.capacity:  # if the cache is now over capacity
            node = self.head.next  # get the ListNode at the front of the linked list (i.e. the least recently used)
            self.remove(node)  # remove the ListNode from the linked list and the cache
            del self.cache[node.key]

    def remove(self, node):
        prevnode = node.prev  # get the previous ListNode in the linked list
        nextnode = node.next  # get the next ListNode in the linked list
        prevnode.next = nextnode  # link the previous node to the next node
        nextnode.prev = prevnode  # link the next node to the previous node

    def add(self, node):
        prevnode = self.tail.prev  # get the ListNode currently at the end of the linked list
        prevnode.next = node  # link the previous node to the new node
        node.prev = prevnode  # link the new node to the previous node

        node.next = self.tail  # link the new node to the dummy tail
        self.tail.prev = node  # link the dummy tail to the new node