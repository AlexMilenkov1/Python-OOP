def reverse_text(str):
    index = len(str) - 1
    end = -1
    while index > end:
        yield str[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')

