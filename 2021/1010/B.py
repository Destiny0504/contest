times = input()

for i in range(int(times)):
    students = input()
    print(students)
    Mon = []
    Tue = []
    Wed = []
    Thu = []
    Fri = []
    total = []
    for i in range(int(students)):
        tmp = input()
        print(f'i:{i} tmp:{tmp}')
        tmp = list(tmp.split())
        for j in range(len(tmp)):
            if tmp[j] == '1':
                if j == 0:
                    Mon.append(i)
                elif j == 1:
                    Tue.append(i)
                elif j == 2:
                    Wed.append(i)
                elif j == 3:
                    Thu.append(i)
                elif j == 4:
                    Fri.append(i)
    total.append(Mon)
    total.append(Tue)
    total.append(Wed)
    total.append(Thu)
    total.append(Fri)
    for i in range(len(total)):
        if len(total[i]) == students // 2:
            tmp = i + 1
            while(tmp < students):
                tmp = tmp + 1
                for j in range(len())

