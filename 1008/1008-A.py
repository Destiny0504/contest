times = input()
for i in range(int(times)):
    tmp1 = 2
    data = input()
    data = int(data)
    while(True):
        if tmp1 % 2 == 0:
            if data % tmp1 == tmp1 // 2:
                print(str(((data // tmp1) - (tmp1 // 2) + 1)) + ' ' + str(((data // tmp1) + (tmp1 // 2))))
                break
            else:
                tmp1 = tmp1 + 1
        else:
            if data % tmp1 == 0:
                print(str(((data // tmp1) - (tmp1 // 2))) + ' ' + str(((data // tmp1) + (tmp1 // 2))))
                break
            else:
                tmp1 = tmp1 + 1