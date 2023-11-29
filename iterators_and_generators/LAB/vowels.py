class vowels:
    def __init__(self, random_string):
        self.random_string = random_string
        my_vowels = ['a', 'u', 'o', 'y', 'e', 'i']
        self.needed_letters = [x for x in self.random_string if x.lower() in my_vowels]
        self.start = 0
        self.end = len(self.needed_letters) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            index = self.start
            self.start += 1
            return self.needed_letters[index]
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
