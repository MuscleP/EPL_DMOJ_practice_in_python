def PossibleNumber(n, k):
    if n == 0 or k == 0:
        return [0]
    li = list(map(lambda x: x+2**(n-1) ,PossibleNumber(n-1, k-1)))
    if n > k:
        li += PossibleNumber(n-1, k)
    return li

T = int(input())
for t in range(1, T+1):
    n, k = input().split()
    li = sorted(PossibleNumber(int(n), int(k)))
    print(f'Case #{t}: {li}')