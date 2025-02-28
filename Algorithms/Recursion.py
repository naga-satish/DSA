class Recursion:
    def __init__(self):
        self.fib_list = [0, 1]

    def factorial(self, num):
        while 0 < num:
            return num * self.factorial(num-1)

        return 1

    def fibonacci(self, num):
        if num == 0:
            return 0
        new_sum = self.fib_list[-1] + self.fib_list[-2]
        while new_sum <= num:
            self.fib_list.append(new_sum)
            return self.fibonacci(num)

        return self.fib_list


if __name__ == "__main__":
    rec = Recursion()
    # print(rec.factorial(10))
    print(rec.fibonacci(1))
    print(rec.fibonacci(11))
    print(rec.fibonacci(100))
    print(rec.fibonacci(1313))
