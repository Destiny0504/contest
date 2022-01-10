times = input()

for itr in range(int(times)):  
    times_2 = input()
    arr = input()
    search = []
    change = True
    arr = list(arr.split())
    times_2 = input()
    for itr2 in range(int(times_2)):
        data = input()
        search.append(list(data.split()))
    counter = 0

    while(change):
        for itr2 in range(len(search)):
            #print(f'int(search[itr2][1]):{int(search[itr2][1])}\ncounter:{counter}')
            if counter == int(search[itr2][1]):
                print(arr[int(search[itr2][0])-1])
                
        counter = counter + 1
        tmp = []
        for data in arr:
            tmp.append(arr.count(data))
        if tmp == arr:
            change = False
        else:
            arr = tmp
        
    for itr2 in range(len(search)):
    #print(f'int(search[itr2][1]):{int(search[itr2][1])}\ncounter:{counter}')
        if counter <=int(search[itr2][1]):
            print(arr[int(search[itr2][0])-1])
    #print(arr[0])
    #print(arr.count(arr[0]))
    #print(arr)
