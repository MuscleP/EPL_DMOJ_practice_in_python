T = int(input())
for case in range(1, T+1):
    candies = input().split()
    numbers_can_eat = len(candies) // 2
    type_of_candies = len(set(candies))
    print(f'Case #{case}: {min(numbers_can_eat, type_of_candies)}')
