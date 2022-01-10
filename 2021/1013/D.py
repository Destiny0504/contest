import math

times = input()
for i in range(int(times)):
    nothing = input()
    data = input()
    data = data.split()
    diff = []
    ans = 1e7
    for itr in range(len(data)):
        data[itr] = int(data[itr])
    for itr in range(len(data) - 1):
        diff.append(abs(data[itr] - data[itr + 1]))
    if max(diff) == 0:
        print(-1)
        continue
    else:
        for itr in range(len(diff) - 1):
            gcd = math.gcd(diff[itr], diff[itr + 1])
            if gcd < ans and gcd > 0:
                ans = gcd
        print(ans)