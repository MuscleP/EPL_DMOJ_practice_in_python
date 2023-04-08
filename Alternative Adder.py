def adder(*args):
    return sum(args[::2]) - sum(args[1::2])

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        args = map(int, input().split())
        print("Case #%d: %d" % (i, adder(*args)))