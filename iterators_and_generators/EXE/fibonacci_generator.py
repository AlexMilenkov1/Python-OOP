def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        yield second_num
        first_num = first_num + second_num
        second_num = first_num + second_num


generator = fibonacci()
for i in range(1):
    print(next(generator))

