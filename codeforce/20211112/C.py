import math
times = input()

for i in range(int(times)):
    length = input()
    data = input()
    cur = 0
    cut = 0
    ans = math.inf
    data = 'd' + data
    if data.count('a') < 2:
        print('-1')
        continue
    while(cur <= int(length)):
        if data[cur] != 'a':
            cur += 1
            continue
        elif cut == 0:
            cut = cur
            cur += 1
        else:
            if data[cut:cur+1].count('b') < 2 and data[cut:cur+1].count('c') < 2 and (cur - cut + 1) < ans:
                ans = (cur - cut + 1)
            cut = cur
            cur += 1
    if ans == 0:
        print('-1')
    else:
        print(ans)
                