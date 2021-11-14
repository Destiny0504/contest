tmp1 = input()
tmp2 = input()
if tmp1 == tmp2:
    print('Yes')
else:
    tmp1 = list(tmp1)
    tmp2 = list(tmp2)
    if len(tmp1) != len(tmp2):
        print('No')
        changed = 1
        failed = 1
    print(tmp1)
    print(tmp2)
    changed = 0
    failed = 0
    for i in range(len(tmp1)):
        print(tmp1[i])
        if tmp1[i] != tmp2[i] and changed == 0:
            tmp = ''
            tmp = tmp1[i]
            tmp1[i] = tmp1[i + 1]
            tmp1[i + 1] = tmp
            changed = changed + 1
            print(changed)
            if tmp1[i] != tmp2[i]:
                failed = 1
                print('No1') 
        elif  tmp1[i] != tmp2[i] and changed > 0 and failed == 0: 
            print('No2')
            break
        else :
            failed = 2
            break
    if failed == 0:
        print('Yes')
    elif failed == 2:
        print('No')