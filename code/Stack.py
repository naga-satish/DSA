class Stack:
    def __init__(self, size=10, auto_resize=False):
        assert size > 0
        self.size = size
        self.length = -1
        self.stack = self._get_stack(size)
        self.auto_resize = auto_resize

    @staticmethod
    def _get_stack(size):
        import ctypes
        return (size * ctypes.py_object)()

    def top(self):
        return self.stack[self.length]

    def resize(self):
        new_size = 2 * self.size
        new_stack = self._get_stack(new_size)
        for index in range(self.length + 1):
            new_stack[index] = self.stack[index]

        self.stack = new_stack
        self.size = new_size

    def push(self, value):
        if self.length < self.size-1:
            self.stack[self.length + 1] = value
            self.length += 1
        elif self.auto_resize:
            self.resize()
            self.stack[self.length + 1] = value
            self.length += 1
        else:
            raise Exception("Stack is Full. Set auto resize to true.")

    def pop(self):
        if self.length > 0:
            temp = self.stack[self.length]
            self.length -= 1
            return temp
        else:
            raise Exception("Empty Stack, no element to pop.")

    def isEmpty(self):
        return self.length == -1

    def isFull(self):
        return self.length == self.size-1

    def __len__(self):
        return self.length + 1

    def __str__(self):
        str_rep = ''
        for idx in range(self.length + 1):
            str_rep += str(self.stack[idx]) + '->'

        return str_rep


if __name__ == "__main__":
    a = Stack(auto_resize=True)
    print("Stack is empty? ", a.isEmpty())
    for i in range(10):
        a.push(i)

    print(len(a), a)

    for i in range(10):
        a.push(i*i)

    for i in range(10):
        a.push(i**i)

    print(len(a), a)
    print("Top element of Stack? ", a.top())
    print("Stack is Empty? ", a.isEmpty())
    print("Stack is Full? ", a.isFull())

