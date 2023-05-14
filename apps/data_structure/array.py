class Array():
    def __init__(self, max: int) -> None:
        self._array = []
        self._max = max

    def append(self, value):
        if self.size() == self._max:
            return -1
        else:
            self._array.append(value)

    def popleft(self):
        return self._array.pop(0)

    def pop(self):
        return self._array.pop()

    def remove(self, value):
        self._array.remove(value)

    def size(self):
        return len(self._array)

    def empty(self):
        return self.size() == 0

    def full(self):
        return self.size() == self._max

    def getFirst(self):
        return self._array[0]

    def getLast(self):
        return self._array[-1]
