class MyRange:
    def __init__(self, end):
        self.n = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.end:
            raise StopIteration
        ret = self.n
        self.n += 1
        return ret


for x in MyRange(10):
    print(x)
