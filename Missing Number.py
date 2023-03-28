T = int(input())
for case in range(1, T+1):
    nums = [int(i) for i in input().split()]
    total = 0
    for n in nums:
        total += n
    missing_number = ((len(nums)+1) * len(nums) >> 1) - total
    print(f'Case #{case}: {missing_number}')  