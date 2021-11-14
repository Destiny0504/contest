times = input()

for i in range(int(times)):
    nothing = input()
    line1 = input()
    line2 = input()
    line1 = list(line1)
    line2 = list(line2)
    find = 1
    for i in range(int(nothing)):
        if line1[i] == '1' and line2[i] == '1':
            find = 0
            print('NO')
            break
    if find == 1:
        print('YES')