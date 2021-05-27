class Queue:

    def __init__(self, q: list):
        self._q = q

    def add(self, element):
        self._q.append(element)

    def remove(self):
        self._q.pop(0)

    def __str__(self):
        return str(self._q).replace(",", "| ")


# queue = Queue([1, 2, 3])
# print(queue)
# queue.add(4)
# queue.add(5)
# print(queue)
# queue.remove()
# print(queue)
# queue.remove()
# print(queue)


class Stack:

    def __init__(self, s):
        self._s = s

    def add(self, element):
        self._s.append(element)

    def remove(self):
        self._s.pop(-1)

    def __str__(self):
        value = ""
        for i in self._s:
            value += i
        return value


stack = Stack(["ab", "c"])
print(stack)
stack.remove()
print(stack)
stack.remove()
print(stack)
stack.add("Hello, ")
stack.add("World")
stack.add("!")
print(stack)
stack.remove()
print(stack)
stack.add(" from Daniiar!")
print(stack)
