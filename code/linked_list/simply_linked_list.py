class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self.length = 0

    def insert_first(self, value: int):
        current_node = Node(value)
        current_node.next = self.head.next
        self.head.next = current_node
        self.length += 1

    def invert(self):
        current_node = self.head.next
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head.next = previous_node

    def remove(self, value: int):
        pass

    def pop_tail(self):
        pass

    def find_value(self, value: int):
        pass

    def find_middle(self):
        pass

    def display(self):
        current_node = self.head.next
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def get_count(self):
        print(f"Number of items: {self.length}")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_first(4)
    ll.insert_first(10)
    ll.insert_first(453)
    ll.insert_first(2)
    ll.display()
    ll.invert()
    ll.display()
    ll.get_count()
