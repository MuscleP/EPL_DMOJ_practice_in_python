def pascal(row, col):
    if (col == 0 or row == col):
        return 1
    return pascal(row - 1, col - 1) + pascal(row - 1, col)
def print_pascal(n):
    if n > 1:
        print_pascal(n-1)
    for i in range(n):
        print(f'{pascal(n-1, i):3d}', end='')
    print()
T = int(input())
for t in range(T):
    n = int(input())
    print_pascal(n)