def sort_by_date(L):
    L.sort(key=lambda x: int(x[2:4]))
    L.sort(key=lambda x: int(x[0:2]))
    L.sort(key=lambda x: int(x[4:8]))
    # L.sort(key=lambda d: (int(d[4:]), int(d[:2]), int(d[2:4])))
# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    date_list = input().split()
    sort_by_date(date_list)
    print(date_list)
