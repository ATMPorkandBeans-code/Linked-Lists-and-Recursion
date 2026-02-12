
class Node:

    def __init__(self, data):
       self.data = data
       self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        def recursive_iterate(current):
            if current == None:
                return 0
            else:
                return current.data + recursive_iterate(current.next)
        return recursive_iterate(self.head)


    def recursive_reverse(self):
        def recursive_helper(current, previous):
            if not current:
                return previous
            next_node = current.next
            current.next = previous
            return recursive_helper(next_node, current)
        self.head = recursive_helper(self.head, None)


    def recursive_search(self, target):
        def search_helper(current):
            if current == None:
                return False
            elif current.data == target:
                return True
            return search_helper(current.next)
        return search_helper(self.head)


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
