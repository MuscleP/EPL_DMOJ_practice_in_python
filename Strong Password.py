from re import search

def is_strong(passwd):
    if len(passwd) >= 8\
        and search(pattern=r'[a-z]', string=passwd) != None\
        and search(pattern=r'[A-Z]', string=passwd) != None\
        and search(pattern=r'[0-9]', string=passwd) != None\
        and search(pattern=r'[-!@#$%^&*()+]', string=passwd) != None\
        and search(pattern=r'(.)\1', string=passwd) == None:
        return True
    else:
        return False

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    passwd = input()
    if is_strong(passwd):
        print('Strong')
    else:
        print('Weak')
