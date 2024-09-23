"""
implement a double-ended queue as a doubly linked list
- push right
- push left
- pop right
- pop left
- size

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def pop_back(self):
        if self.head is None:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data


class Node1(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque1(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def push_right(self, val):
        n = Node(val)
        if self.size > 0:
            self.head.next = n
        n.prev = self.head
        self.head = n
        self.size += 1


if __name__ == "__main__":
    d = Deque()
    # test basic push/pop right (stack semantics)
    assert d.size == 0
    val = "foo"
    d.push_right(val)
    assert d.size == 1
    assert d.pop_right is val
    assert d.size == 0
    print("ok")
