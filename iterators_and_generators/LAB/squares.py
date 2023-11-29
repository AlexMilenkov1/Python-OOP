def squares(n):
    end = n
    number = 1

    while number <= end:
        yield number ** 2
        number += 1


for num in squares(5):
    print(num)
