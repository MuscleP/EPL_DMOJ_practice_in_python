for i in range(1, int(input())+1):
    N = int(input())
    N <<= 1
    if N >= 0b1_0000_0000:
        N = N ^ 0b1_0000_0001
    print(f'Case #{i}: {N}')