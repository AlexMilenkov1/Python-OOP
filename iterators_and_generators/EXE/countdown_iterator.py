class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        while self.count >= 0:
            number = self.count
            self.count -= 1
            return number
        else:
            raise StopIteration()


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
