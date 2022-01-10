times = int(input())

for itr1 in range(times):
    data = list(map(lambda x : int(x),input().split()))
    ans = 0
    for_start = ((2 * data[1]) - data[2]) // data[0]
    for_mid = (data[2] - data[0]) // data[1]
    for_end = ((2 * data[1]) - data[0]) // data[2]
    print(f'start : {for_start} mid : {for_mid} end : {for_end}')
    if (((2 * data[1]) - data[2]) - abs(data[0] * for_start)) == 0:
        ans = 1
    if ((data[2] - data[0]) - abs(data[1] * for_mid)) == 0:
        ans = 1
    if (((2 * data[1]) - data[0]) - abs(data[2] * for_end)) == 0:
        ans = 1
    if ans :
        print('YES')
    else:
        print('NO')