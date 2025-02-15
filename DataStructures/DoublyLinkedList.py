class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.length != 0:
            self.head.prev = new_node
        self.head = new_node
        if self.length == 0:
            self.tail = new_node

        self.length += 1

    def insert_at_idx(self, idx, value):
        assert 0 <= idx < self.length
        if idx == 0:
            self.insert(value)
        elif idx == self.length-1:
            self.insert_at_tail(value)
        else:
            count = 0
            new_node = Node(value)
            prev = None
            temp = self.head

            while count < idx:
                prev = temp
                temp = temp.next
                count += 1

            new_node.prev = prev
            new_node.next = temp
            prev.next = new_node

            self.length += 1

    def insert_at_tail(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def get_head(self):
        if self.length != 0:
            return self.head.value
        else:
            print(f"No Head. Empty {self.__class__.__name__} instance.")

    def get_tail(self):
        if self.length != 0:
            return self.tail.value
        else:
            print(f"No Tail. Empty {self.__class__.__name__} instance.")

    def delete_head(self):
        if self.length > 0:
            self.head = self.head.next
            if self.length > 1:
                self.head.prev = None

            self.length -= 1
        else:
            print(f"No head to delete. Empty {self.__class__.__name__} object")

    def delete_tail(self):
        if self.length > 0:
            print("level 1")
            self.tail = self.tail.prev
            if self.length > 1:
                print("level 2")
                self.tail.next = None

            self.length -= 1
        else:
            print(f"No tail to delete. Empty {self.__class__.__name__} object")

    def delete(self, by: str = None, index: int = None, value=None):
        f"""
        delete element from this {self.__class__.__name__}.
        pass index as value to 'by' parameter to delete by index or pass element to delete by value
        :param by: delete based on this value. Should be either index or value
        :param index: index to be removed. Should be
        :param value: pass value that needs to be removed
        :return: returns None, prints if element is deleted or not
        """
        by = by.lower().strip()
        assert by in ('index', 'value')
        if by == 'index':
            assert 0 <= index < self.length
            if index == 0:
                self.delete_head()
            elif index == self.length-1:
                self.delete_tail()
            else:
                if index <= (self.length-1)/2:
                    temp = self.head
                    count = 0
                    while count < index:
                        count += 1
                        temp = temp.next
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:
                    temp = self.tail
                    count = self.length-1
                    while count > index:
                        count -= 1
                        temp = temp.prev
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next

                self.length -= 1
        else:
            if self.length > 0:
                count = 0
                temp = self.head
                prev = None
                while count < self.length:
                    if temp.value == value:
                        if count == 0:
                            temp.next.prev = None
                            self.head = temp.next
                        else:
                            prev.next = temp.next

                        if count != self.length-1:
                            temp.next.prev = prev

                        self.length -= 1
                        break

                    prev = temp
                    temp = temp.next
                    count += 1
            else:
                print(f"Can't delete from an empty {self.__class__.__name__} instance!.")

    def reverse(self):
        reversed_ll = DoublyLinkedList()
        temp = self.head

        while temp.next or temp.value:
            reversed_ll.insert(temp.value)
            if temp.next is None:
                break
            temp = temp.next
        return reversed_ll

    def __len__(self):
        return self.length

    def __str__(self):
        if self.length == 0:
            return f'Empty {self.__class__.__name__} instance.'
        else:
            str_rep = ''
            temp = self.head
            while temp.next:
                if not isinstance(temp.value, str):
                    str_rep = str_rep + str(temp.value) + " <-> "
                else:
                    str_rep = str_rep + f"'{str(temp.value)}' <-> "

                if not temp.next:
                    break
                temp = temp.next

            if not isinstance(temp.value, str):
                str_rep = str_rep + str(temp.value)
            else:
                str_rep = str_rep + f"'{str(temp.value)}'"

            return str_rep


if __name__ == "__main__":
    a = DoublyLinkedList()
    # print(a)

    for i in range(1, 11):
        a.insert(i**i)

    print(a, '|', len(a))
    print(f"head - {a.get_head()}, tail - {a.get_tail()}")
    a.insert_at_tail(5)
    print(a, '|', len(a))
    print(f"tail - {a.get_tail()}")
    print('\n\ndelete')

    a.delete_head()
    print(a, '|', len(a))

    a.delete_tail()
    print(a, '|', len(a))

    a.delete(by='value', value=10000)
    print(a, '|', len(a))

    print('delete\n\n')

    a.insert_at_idx(0, 5)
    print(a, '|', len(a))

    print(a.reverse(), '|', len(a))
    print(a, '|', len(a))
