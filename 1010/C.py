times = input()

for i in range(int(times)):
    nothing = input()
    data = input()
    data = list(data.split())
    for i in range(len(data)):
        data[i] = int(data[i])
    if sum(data) / len(data) > (sum(data) // len(data)):
        print(0)
    else:
        total = 2 * (sum(data) // len(data))
        ans = 0
        i = 0
        for i in range(len(data)):
            ans = ans + data.count(total - data[i])
            if data[i] == total // 2:
                ans = ans - 1
        print(ans // 2)