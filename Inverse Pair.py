T = int(input())
for case in range(1, T+1):
    li = [int(i) for i in input().split()]
    number_of_pairs = 0
    while len(li) > 0:
        p = li.pop(0)
        for l in li:
            if p > l:
                number_of_pairs += 1
    print(f'Case #{case}: {number_of_pairs}')  