times = input()

for i in range(int(times)):    
    nothing = input()
    n, k = nothing.split()
    n = int(n)
    k = int(k)
    data = input()
    data = data.split()
    for itr in range(len(data)):
        data[itr] = abs(int(data[itr]) - n)
    data.sort()
    j = 0 
    tmp = 0
    while(j < len(data)):
        if (tmp + data[j]) < n:
            tmp = tmp + data[j]
        else:
            break
        j = j + 1
    print(j)
    