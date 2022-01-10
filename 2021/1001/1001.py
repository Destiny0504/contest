times = input()
times = int(times)
for i in range(times):
    deepth = input()
    deepth, step = deepth.split()
    deepth = int(deepth)
    step = int(step)
    total = ((2 ** deepth) - 1)
    killed = 0
    nodes = []
    answer = 0
    if deepth > 0:
        nodes.append(1)
    while(killed < total):
        answer = answer + 1
        tmp_list = []
        
        for i in range(step):
            if nodes != []:
                killed = killed + 1
                tmp = nodes.pop(0)
                
                tmp_list.append(2 * tmp)
                tmp_list.append(2 * tmp + 1)
        for items in tmp_list:
            nodes.append(items)
        
    print(answer)
