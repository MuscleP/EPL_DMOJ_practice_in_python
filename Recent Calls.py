class RecentCounter:

    def __init__(self):
        self.count = 0
        self.record = []
    def ping(self, t):
        self.count += 1
        self.record.append(t)
        while len(self.record) > 0:
            if self.record[0] < t - 3000:
                self.count -= 1
                del self.record[0]
            else:
                break
        return self.count

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(1,T+1):
    counter = RecentCounter()
    calls = list(map(int,input().split()))
    for ind,time in enumerate(calls):
        print(f'Case #{t}_{ind}: {counter.ping(time)}')