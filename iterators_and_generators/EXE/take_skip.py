class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = 0
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_count < self.count:
            current_num = self.number
            self.number += self.step
            self.current_count += 1
            return current_num
        else:
            raise StopIteration()


numbers = take_skip(2, 6)

for number in numbers:
    print(number)
