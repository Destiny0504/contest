times = input()

for itr in range(int(times)):
    data = input()
    a = min(data)
    for itr2 in range(len(data)):
        if data[itr2] == a:
            data = data[:itr2] + data[itr2 + 1:]
            break
    print(a + ' ' + data)
