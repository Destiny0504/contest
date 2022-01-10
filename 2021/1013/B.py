times = input()

for i in range(int(times)):
    data = input()
    data = list(data)
    find_five = False
    five = False
    remove_for_five = 0
    find_zero = False
    zero = False
    remove_for_zero = 0
    for i in range(len(data)):
        data[i] = int(data[i])
    for i in range(len(data)):
        if data[-i - 1] == 0:
            if find_zero == False:
                remove_for_five = remove_for_five + 1
                find_zero = True 
                continue
            else:
                zero = True
                break
        if data[-i - 1] == 2:
            if find_five == True:
                five = True
                break
            else:
                remove_for_zero = remove_for_zero + 1
                remove_for_five = remove_for_five + 1
                continue
        if data[-i - 1] == 5 :
            if find_zero == True:
                zero = True
                break
            if find_five == True:
                remove_for_five = remove_for_five + 1
            else:
                find_five = True
            remove_for_zero = remove_for_zero + 1
            continue
        if data[-i - 1] == 7:
            if find_five == True:
                five = True
                break
            else:
                remove_for_zero = remove_for_zero + 1
                remove_for_five = remove_for_five + 1
                continue
        remove_for_five = remove_for_five + 1
        remove_for_zero = remove_for_zero + 1
        #print(f'find zero:{find_zero} remove for zero : {remove_for_zero} find five : {find_five} remove for five:{remove_for_five}')
    if five:
        print(remove_for_five)
    else:
        print(remove_for_zero)