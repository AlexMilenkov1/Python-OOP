n = int(input())

for row in range(1, n + 1):
    print(' ' * (n - row), end='')
    print(*['*'] * row)

for row in range(1, n):
    print(' ' * row, end='')
    print(*['*'] * (n - row))
