import math
import copy
def swap(string):
    tmp_list = []
    for i in range(len(string) - 1):
        tmp_char1 = string[i]
        tmp_char2 = string[i + 1]
        #print(tmp_char1)
        if string[i] != string[i + 1]:
            tmp = string[:i] + tmp_char2 + tmp_char1 + string[i + 2:]
            #print(tmp)
            #print(f'curr i:{i}')
            tmp_list.append(tmp)
    return tmp_list
        
data = input()
K = input()
K = int(K)
cur_list = []
next_swap = []
cur_list.append(data)
next_swap.append(data)
max_len = ((math.factorial(len(data)) // math.factorial(data.count('K'))) // math.factorial(data.count('E'))) // math.factorial(data.count('Y'))
if K >= 50 :
    print(max_len)
    exit()
while(len(cur_list) < max_len and K > 0):
    K -= 1
    #print(f'K : {K}')
    for_swap = copy.deepcopy(next_swap)
    new_list = copy.deepcopy(cur_list)
    next_swap = []
    for string in for_swap:
        for each_swapped in swap(string):
            #print(f'string : {string}')
            if each_swapped not in new_list:
                new_list.append(each_swapped)
                next_swap.append(each_swapped)
    cur_list = new_list
print(len(cur_list))