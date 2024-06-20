class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


my_iterable = MyIterable(1, 5)

for element in my_iterable:
    print(element)



