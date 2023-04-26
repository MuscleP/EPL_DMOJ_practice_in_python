def fib(n):
    if n in (0, 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
T = int(input())
for t in range(T):
    n = int(input())
    print(fib(n))   