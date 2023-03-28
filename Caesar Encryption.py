import string

T = int(input())
for case in range(1, T+1):
    S = input()
    text = ''
    for c in S:
        if c == 'z':
            text += 'a'
        elif c == 'Z':
            text += 'A'
        elif c in string.ascii_letters:
            text += string.ascii_letters[string.ascii_letters.index(c)+1]
        else:
            text += c
    print(f'Case #{case}: {text}')  