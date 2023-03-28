T = int(input())
for case in range(1, T+1):
    arr = input().split()
    arr.reverse()
    carry = 1
    for index, _ in enumerate(arr):
        arr[index] = int(arr[index])
        arr[index] += carry
        carry = 0
        if arr[index] >= 10:
            arr[index] -= 10
            carry = 1
    if carry == 1:
        arr.append(carry)
    arr.reverse()
    print(f'Case #{case}: {arr}')