from itertools import permutations
def permute(nums):
    return [list(num) for num in permutations(nums)]

T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))
    print(permute(nums))