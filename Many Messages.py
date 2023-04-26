from math import ceil
current = int(input())
step = int(input())
received_message = int(input())

for i in range(1, 4):
    current += step
    if received_message <= current:
        print(current)
        break
else:
    print('Who knows...')