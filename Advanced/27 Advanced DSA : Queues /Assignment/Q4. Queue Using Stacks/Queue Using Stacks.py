class UserQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.Queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.Queue) > 0:
            return self.Queue.pop(0)
        return -1

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.Queue) > 0:
            return self.Queue[0]
        return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.Queue) > 0:
            return False
        return True

# Your UserQueue object will be instantiated and called as such:
# obj = UserQueue()
# obj.push(x)
# param2 = obj.pop()
# param3 = obj.peek()
# param4 = obj.empty()