class Node(object):

    def __init__(self, data, next_node=None):
        self.next = next_node
        self.data = data

    def __str__(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insert_to_front(self, data):
        if data is None:
            return
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return node

    def append(self, data, next_node=None):
        if data is None:
            return
        node = Node(data, next_node)
        if self.head is None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = node
        return node

    def find(self, data):
        if data is None:
            return
        if self.head is None:
            return
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            else:
                curr_node = curr_node.next
        return

    def delete(self, data):
        if data is None:
            return
        if self.head is None:
            return
        prev_node = self.head
        curr_node = prev_node.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data