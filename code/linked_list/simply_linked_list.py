from collections import defaultdict


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node value: {self.value}, Neighbor: {self.next}"

    def __repr__(self):
        return f"Node(value='{self.value}', neightbor={self.next})"


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
        current_node = self.head.next
        previous_node = None
        while current_node:
            if current_node.value == value:
                previous_node.next = current_node.next
                self.length -= 1
            previous_node = current_node
            current_node = current_node.next

    def pop_tail(self):
        pass

    def find_value(self, value: int):
        current_node = self.head.next
        node_count = 0
        while current_node:
            if current_node.value == value:
                print(f"Value {current_node.value} found at node {node_count}")
                break
            node_count += 1
            current_node = current_node.next

    def find_middle(self):
        fast_ptr, slow_ptr = self.head.next, self.head.next
        while slow_ptr and slow_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next.next
        print(f"Middle value: {fast_ptr.value}")

    def display(self):
        current_node = self.head.next
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def get_count(self):
        print(f"Number of items: {self.length}")

    def most_frequent_value(self):
        current_node = self.head.next
        frequency_map = defaultdict(int)
        while current_node:
            frequency_map[current_node.value] += 1
            current_node = current_node.next
        print(f"Most frequent value: {max(frequency_map,key=frequency_map.get)}")

    def rotate_list(self, iterations: int):
        slow_ptr, fast_ptr = self.head.next, self.head.next
        iterations %= self.length
        count = 0
        while count < iterations:
            fast_ptr = fast_ptr.next
            count += 1
        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        new_head = slow_ptr.next
        slow_ptr.next = None
        fast_ptr.next = self.head.next
        self.head.next = new_head

    def insert_at_position(self, value, position):
        if self.length == 0:
            print("Cannot insert at a given position in an empty list")
            return
        current_node = self.head.next
        previous_node = self.head
        position %= self.length
        count = 0
        while count < position and current_node:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        new_node = Node(value)
        previous_node.next = new_node
        new_node.next = current_node
        self.length += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_first(4)
    ll.insert_first(10)
    ll.insert_first(453)
    ll.display()
    ll.insert_first(2)
    ll.display()
    ll.find_value(453)
    ll.invert()
    ll.display()
    ll.get_count()
    ll.find_middle()
    ll.find_value(453)
    ll.remove(453)
    ll.display()
    ll.insert_first(3)
    ll.insert_first(2)
    ll.insert_first(134)
    ll.most_frequent_value()
    print("Before rotate")
    ll.display()
    ll.rotate_list(2)
    ll.display()
    print("Inserting 3000 at position 1")
    ll.insert_at_position(3000, 1)
    ll.display()
