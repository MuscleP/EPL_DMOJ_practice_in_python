def reverse(L):
    rL = []
    for l in L[::-1]:
        if type(l) == list:
            rL.append(reverse(l))
        else:
            rL.append(l)
    return rL

T = int(input())
for t in range(T):
    L = eval(input())
    rL = reverse(L)
    print(L)
    print(rL)