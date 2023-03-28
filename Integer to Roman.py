T = int(input())
for case in range(1, T+1):
    N = int(input())
    roman = ''
    while N > 0:
        if N >= 1000:
            N -= 1000
            roman += 'M'
        elif N >= 900:
            N -= 900
            roman += 'CM'
        elif N >= 500:
            N -= 500
            roman += 'D'
        elif N >= 400:
            N -= 400
            roman += 'CD'
        elif N >= 100:
            N -= 100
            roman += 'C'
        elif N >= 90:
            N -= 90
            roman += 'XC'
        elif N >= 50:
            N -= 50
            roman += 'L'
        elif N >= 40:
            N -= 40
            roman += 'XL'
        elif N >= 10:
            N -= 10
            roman += 'X'
        elif N >= 9:
            N -= 9
            roman += 'IX'
        elif N >= 5:
            N -= 5
            roman += 'V'
        elif N >= 4:
            N -= 4
            roman += 'IV'   
        elif N >= 1:
            N -= 1
            roman += 'I'
        else:
            break
    print(f'Case #{case}: {roman}')