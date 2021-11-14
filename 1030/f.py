times = input()
n, k = times.split()
n = int(n)
k = int(k)
data = []
for itr in range(n):  
    tmp = input()
    data.append(tmp)
for i in range(k-1):
    for itr1 in range(n):
        for itr2 in range(itr1 + 1, n):
            if data[itr1] + data[itr2] > data[itr2] + data[itr1]:
                tmp = data[itr2]
                data[itr2] = data[itr1]
                data[itr1] = tmp
    data[1] = data[0] + data[1]
    data = data[1:]
    n -= 1

print(data[0])