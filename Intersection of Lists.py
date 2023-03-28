T = int(input())
for case in range(1, T+1):
    nums1 = [int(s) for s in input().split()]
    nums2 = [int(s) for s in input().split()]
    intersection = sorted(list(set(nums1) & set(nums2)))
    print(f'Case #{case}: {intersection}')
    