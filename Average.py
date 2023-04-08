def aver(*nums):
    return sum(nums) / len(nums)

T = int(input())
for t in range(T):
    nums = [int(n) for n in input().split()]
    mean = aver(*nums)
    print(f'{mean}')