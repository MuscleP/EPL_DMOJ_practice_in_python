T = int(input())
for case in range(1, T+1):
    L = input().split()
    print(f'Case #{case}: ', end='')
    if L == list(reversed(L)):
#   if L == L[::-1]:
        print('Yes')
    else:
        print('No')
