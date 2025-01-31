import ctypes


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Method to insert elements at the start of the LinkedList.
        This will update the head of teh lInkedList to the node that is being inserted.
        :param value: Value to be inserted.
        :return: None
        """
        # 1. Create New Node
        new_node = Node(value)
        # 2. Assign next head as next node to the new  node
        new_node.next = self.head
        # 3. Make the new node as new head
        self.head = new_node

    def find(self, value):
        """
        :param value: value to be searched for from the LinkedList
        :return:
            -1 if you are searching an Empty LinkedList
            True if the element you are searching is found
            False if the element you are searching is found
        """
        if self.head is None:
            return -1
        else:
            current_node = self.head
            if current_node.value == value:
                return True

            while current_node.next:
                if current_node.value == value:
                    return True
                current_node = current_node.next

            return False

    def insert_at_end(self, value):
        """
        Method to insert elements at the end of the LinkedList.
        :param value: Value to be inserted at the end of the LinedList.
        :return: None
        """
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        new_node = Node(value)

        current_node.next = new_node


a = SingleLinkedList()

print(a.find)

for i in range(10):
    a.insert(i**3)

print(a.head.value)
print(a.find(3))
