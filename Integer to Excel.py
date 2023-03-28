from string import ascii_uppercase
T = int(input())
for case in range(1, T+1):
    N = int(input())
    title = ''
    while N > 0:
        N = N-1
        title = ascii_uppercase[N % 26] + title
        N //= 26
    print(f'Case #{case}: {title}')