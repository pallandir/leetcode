class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, value):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.value == value:
                previous_node.next = current_node.next
                self.length -= 1
            previous_node = current_node
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def invert(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(5)
    linked_list.append(2)
    linked_list.display()
    linked_list.remove(5)
    linked_list.display()
    linked_list.append(30)
    linked_list.display()
    linked_list.invert()
   linked_list.display()
