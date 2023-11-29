class reverse_iter:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.start_index = len(self.iterable_object) - 1
        self.end_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.end_index < self.start_index:
            current_index = self.start_index
            self.start_index -= 1
            return self.iterable_object[current_index]
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

