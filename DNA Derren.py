DNA = input()
state = 'consonant'
if DNA[0] == 'A':
    state = 'vowel'
else:
    state = 'consonant'
print(DNA[0], end='')
for i in DNA[1:]:
    if state == 'vowel':
        if i == 'A':
            print('', i, end='')
        else:
            print(i, end='')
            state = 'consonant'
    elif state == 'consonant':
        if i == 'A':
            print(i, end='')
            state = 'vowel'
        else:
            print('', i, end='')
    else:
        print('invalid')
        
    