class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

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
        self.length += 1

    def find(self, value):
        """
        :param value: value to be searched for from the LinkedList
        :return:
            -1 if you are searching an Empty LinkedList
            True if the element you are searching is found
            False if the element you are searching is found
        """
        if self.head is not None:
            item = self.head
            if item.value == value:
                return True

            while item.next:
                if item.value == value:
                    return True
                item = item.next

            return False
        else:
            return -1

    def insert_at_end(self, value):
        """
        Method to insert elements at the end of the LinkedList.
        :param value: Value to be inserted at the end of the LinedList.
        :return: None
        """
        if self.head is not None:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)
            self.length += 1
        else:
            self.insert(value)

    def insert_at(self, at, value):
        try:
            assert 0 <= at <= self.length

            if at == 0:
                self.insert(value)
                return True
            elif at == self.length:
                self.insert_at_end(value)
                return True
            else:
                current_idx = 0
                new_node = Node(value)
                temp = self.head
                while current_idx < at:
                    if current_idx == at-1:
                        new_node.next = temp.next
                        temp.next = new_node
                        self.length += 1
                        return True

                    current_idx += 1
                    temp = temp.next

            return False
        except AssertionError:
            print(f"Index to insert at should be in between 0 and {self.length - 1} (Inclusive)")

    def delete(self, value):
        assert 0 < self.length
        count = 0
        deleted = False

        temp = self.head
        prev = None
        while count < self.length:
            if temp.value == value:
                if count == 0:
                    if temp.next:
                        self.head = temp.next
                    else:
                        self.head = None
                elif count == self.length-1:
                    prev.next = None
                else:
                    prev.next = temp.next
                deleted = True
                self.length -= 1
                break

            count += 1
            prev = temp
            temp = temp.next

        if deleted:
            print(f"{value} deleted.")
        else:
            print("No such element.")

    def delete_head(self):
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None

            self.length -= 1

    def delete_tail(self):
        count = 0
        temp = self.head
        while count < self.length - 2:
            count += 1
            temp = temp.next
        temp.next = None
        self.length -= 1

    def delete_idx(self, idx):
        assert 0 <= idx < self.length
        if idx == 0:
            self.delete_head()
        elif idx == self.length-1:
            self.delete_tail()
        else:
            count = 0
            temp = self.head
            prev = None
            while count < idx:
                prev = temp
                temp = temp.next
                count += 1

            prev.next = temp.next
            self.length -= 1

    def value_at(self, idx):
        assert 0 <= idx <= self.length-1
        count = 0
        temp = self.head
        while count < idx:
            count += 1
            temp = temp.next
        return temp.value

    def front(self):
        return self.head.value

    def back(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.value

    def reversed(self):
        reversed_ll = SinglyLinkedList()
        temp = self.head

        while temp.next or temp.value:
            reversed_ll.insert(temp.value)
            if temp.next is None:
                break
            temp = temp.next
        return reversed_ll

    def empty(self):
        return True if self.length == 0 else False

    def __len__(self):
        return self.length

    def __str__(self):
        temp = self.head
        str_rep = ''
        if temp:
            if not temp.next:
                str_rep = str(temp.value) if type(temp.value) is not str else f'"{temp.value}"'
                return str_rep

            while temp.next:
                str_rep = str_rep + (str(temp.value) if type(temp.value) is not str else f'"{temp.value}"') + ' -> '
                temp = temp.next

            str_rep += (str(temp.value) if type(temp.value) is not str else f'"{temp.value}"')

        return str_rep


a = SinglyLinkedList()

for i in range(12):
    a.insert(i)

# print(a, '\n')
# a.insert_at_end(10)
# print(a, '\n')
# a.insert_at(12, 0)
# print(a, '\n')
# a.delete(10)
# print(a, '\n')
# print(a.length, '\n')
# print(a, '\n')
# a.delete_head()
# print(a.length, ' | ', a, '\n')
#
# a.delete_tail()
# print(a.length, ' | ', a, '\n')
#
# print(a.value_at(5), ' | ', a, '\n')
# print(a.front(), ' | ', a, '\n')
# print(a.back(), ' | ', a, '\n')
#
# print(a.delete_idx(9), ' | ', a, '\n')
#
# print(a)
# a = a.reversed()
# print(a)
