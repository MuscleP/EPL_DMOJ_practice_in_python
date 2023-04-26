T = int(input())
for case in range(1, T+1):
    N = int(input())
    D = [int(d) for d in input().split()]
    current_level = 0
    pay = 0
    while len(D) > 0:
        if D[0] < D[-1]:
            d = D.pop(0)
        else:
            d = D.pop(-1)
        if d >= current_level:
            current_level = d
            pay += 1
    print(f'Case #{case}: {pay}')