T = int(input())
for case in range(1, T+1):
    S = input()
    R = int(input())
    if len(S) is not 0:
        R %= len(S)
    else:
        R = 0
    print(f'Case #{case}: {S[R:]}{S[:R]}')