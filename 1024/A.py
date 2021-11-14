times = input()

for itr in range(int(times)):
    data = input()
    data = list(data.split())
    for itr2 in range(len(data)):
        data[itr2] = int(data[itr2])
    total = data[0] + 2 * data[1] + 3 * data[2] 
    if total % 2 == 1:
        print(1)
    else:
        print(0)