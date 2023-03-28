T = int(input())
for case in range(1, T+1):
    c = input()
    number = 0
    for a in c:
        number *= 26
        number += ord(a) - ord('A') + 1
    print(f'Case #{case}: {number}')