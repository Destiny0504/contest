times = input()

for itr in range(int(times)):
    length = input()
    arr_a = input()
    arr_b = input()
    arr_a = list(arr_a.split())
    arr_b = list(arr_b.split())
    for itr2 in range(int(length)):
        arr_a[itr2] = int(arr_a[itr2])
        arr_b[itr2] = int(arr_b[itr2])
    arr_a = sorted(arr_a)
    arr_b = sorted(arr_b)
    test  = True
    for itr2 in range(int(length)):
        if int(arr_b[itr2]) - int(arr_a[itr2]) > 1:
            test = False
            break
    if test:
        print('YES')
    else:
        print('NO')