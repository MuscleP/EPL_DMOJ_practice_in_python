class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.li = [''] * (n+1)
        self.pointer = 1

    def insert(self, idKey: int, value: str):
        self.li[idKey] = value
        chunk = []
        while self.pointer < self.n+1 and self.li[self.pointer] != '':
            chunk.append(self.li[self.pointer])
            self.pointer += 1
        return chunk


stream = OrderedStream(5)
print(stream.insert(3, "ccccc"))
print(stream.insert(1, "aaaaa"))
print(stream.insert(2, "bbbbb"))
print(stream.insert(5, "eeeee"))
print(stream.insert(4, "ddddd"))