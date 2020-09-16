class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        new_next = value
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1

        else:
            new_node.set_next_node(self.head)
            self.head = new_node
            self.count += 1

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1

        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
            self.count += 1

    def remove_head(self):
        if self.head is None:
            return None

        else:
            ret_value = self.head.get_value()

            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.count = 0

            else:
                self.head = self.head.get_next_node()
                self.count -= 1

            return ret_value

    def remove_tail(self):
        if self.tail is None:
            return None

        else:
            ret_value = self.tail.get_value()

            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.count = 0

            else:
                self.tail = self.head.get_next_node()
                self.count -= 1

            return ret_value

    

    def contains(self, value):
        # loop through LL until pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find a value
            if cur_node.get_value() == value:
                return True
        return False

    def get_max(self):
        # to do

        pass
