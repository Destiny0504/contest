times = input()

for i in range(int(times)):
    length = input()
    data = input()
    tmp = sorted(data)
    ans = []
    for i in range(len(data)):
        if data[i] != tmp[i]:
            ans.append(str(i+1))
    if len(ans) != 0:
        print(1)
        print(str(len(ans)) + ' ' + ' '.join(ans))
    else:
        print(0)
