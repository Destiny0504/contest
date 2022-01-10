times = input()

for itr in range(int(times)):
    nothing = input()
    data = input()
    data = list(data.split())
    tmp = []
    for number in data:
        tmp.append(bin(int(number))[2:].zfill(30))
    data = []
    for itr2 in range(30):
        count = 0
        for itr3 in range(int(nothing)):
            
            if tmp[itr3][-itr2 - 1] == '1': 
                count = count + 1
        data.append(count)
    tmp = filter(lambda b : b > 0, data)
    print(tmp)
    print(data)