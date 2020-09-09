"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print_list(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print("---")

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):

        new_node = ListNode(value, None, self.head)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        # self.head = new_node

        # last = self.head

        # while last.next is not None:
        #     last = last.next

        # last.next = new_node

        # new_node.prev = last

        self.length += 1

        # return

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):

        removed = self.head.value

        # if there is no head then there's nothing to remove
        if self.head is None:
            return None

        if not self.head.next:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed

        # new head is the next item of the removed item
        self.head = self.head.next

        # fix length
        self.length -= 1

        return removed

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):

        new_node = ListNode(value)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current
            new_node.next = None
            self.tail = new_node
            self.length += 1

        # new_node = ListNode(value)

        # if self.length == 0:
        #     self.head = new_node
        #     self.tail = new_node
        #     self.length += 1

        # else:
        #     prv = self.tail
        #     prv.next = new_node
        #     self.tail = new_node
        #     self.tail.prev = prv
        #     self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):

        removed = self.tail.value

        if not self.head and not self.tail:
            return None

        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed

        else:
            current = self.head

            while current.next:
                current = current.next

            self.tail = current.prev
            self.tail.next = None
            self.length -= 1
            return removed

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):

        if self.length == 0:
            return

        elif node == self.head:
            return

        elif node == self.tail:
            prv = node.prev
            prv.next = None
            self.tail = prv
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
            return

        else:
            prv = node.prev
            nxt = node.next
            prv.next = nxt
            nxt.prev = prv
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            return

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):

        if self.length == 0:
            return

        elif node == self.tail and not self.head:
            return

        elif node == self.head and not self.tail:
            nxt = self.head.next
            nxt.prev = None
            self.head = nxt
            node.prev = self.tail
            node.next = None
            self.tail = node

        elif node == self.head and node == self.tail:
            return

        else:
            nxt = node.next
            prv = node.prev
            nxt.prev = prv
            # prv.next = nxt
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):

        current = self.head

        while current:
            if current == node and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    self.tail = None
                    self.length -= 1
                    return

                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    self.length -= 1

                    return

            elif current == node:
                if current.next:
                    nxt = current.next
                    prv = current.prev
                    prv.next = nxt
                    nxt.prev = prv
                    current.next = None
                    current.prev = None
                    current = None
                    self.length -= 1

                    return

                else:
                    prv = current.prev
                    prv.next = None
                    current.prev = None
                    current = None
                    self.tail = prv
                    self.length -= 1

                    return

            current = current.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):

        current = self.tail

        mx = self.tail.value

        while current.prev:
            self.print_list()

            if int(current.value) > mx:
                mx = current.value

            current = current.prev

        return mx
