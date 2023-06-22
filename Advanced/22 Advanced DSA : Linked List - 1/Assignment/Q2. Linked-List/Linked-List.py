class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LL:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_node(self, position, value):
        if position > (self.length + 1):
            return

        newNode = Node(value)
        temp = self.head
        if position == 1:
            newNode.next = temp
            self.head = newNode
        else:
            c = 1
            while c < position - 1:
                temp = temp.next
                c += 1
            newNode.next = temp.next
            temp.next = newNode
        self.length += 1

    def delete_node(self, position):
        if position > (self.length):
            return
        else:
            temp = self.head
            if position == 1:
                newHead = temp.next
                self.head = newHead

            else:
                count = 1
                while count < position - 1:
                    temp = temp.next
                    count += 1

                new_node = temp.next.next
                temp.next = new_node

            self.length -= 1

    def print_ll(self):
        if self.head:
            temp = self.head
            while temp.next:
                print(temp.data, end=" ")
                temp = temp.next

            if temp:
                print(temp.data, end="")
            print()


ll = LL()


def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    return ll.insert_node(position, value)


def delete_node(position):
    # @param position, integer
    # @return an integer
    return ll.delete_node(position)


def print_ll():
    # Output each element followed by a space
    return ll.print_ll()
