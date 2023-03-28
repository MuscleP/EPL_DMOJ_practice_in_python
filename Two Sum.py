T = int(input())
for case in range(1, T+1):
    t = int(input())
    L = sorted([[int(l), id] for id, l in enumerate(input().split())])
    left = 0
    right = len(L)-1
    while left < right:
        if L[left][0] + L[right][0] < t:
            left += 1
        elif L[left][0] + L[right][0] > t:
            right -= 1
        else:
            print(f'Case #{case}: {sorted([L[left][1], L[right][1]])}')
            break
    else:
        print('No answer!')
    
        