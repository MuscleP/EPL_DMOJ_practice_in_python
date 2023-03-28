T = int(input())
for case in range(1, T+1):
    c1, c2 = (input().split())
    c1 = complex(c1)
    c2 = complex(c2)
    a = c1.real
    b = c1.imag
    c = c2.real
    d = c2.imag
    if a > c and b > d:
        sign = '>'
    elif a < c and b < d:
        sign = '<'
    elif a == c and b == d:
        sign = '=='
    elif (a == c and b > d) or (a > c and b == d):
        sign = '>='
    elif (a == c and b < d) or (a < c and b == d):
        sign = '<='
    else:
        sign = '!='
    print(f'Case #{case}: {c1} {sign} {c2}') 