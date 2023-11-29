def genrange(start, end):
    number = start

    while number <= end:
        yield number
        number += 1


for num in genrange(1, 10):
    print(num)
