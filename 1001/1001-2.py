import math
times = input()
times = int(times)
for i in range(times):
    deepth = input()
    deepth, step = deepth.split()
    deepth = int(deepth)
    step = int(step)
    height = 0
    total = ((2 ** deepth) - 1)
    killed = 0
    answer = 0
    tmp_ans = 0
    more = 0
    tmp = 1
    tmp_list = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647, 4294967295, 8589934591, 17179869183, 34359738367, 68719476735, 137438953471, 274877906943, 549755813887, 1099511627775, 2199023255551, 4398046511103, 8796093022207, 17592186044415, 35184372088831, 70368744177663, 140737488355327, 281474976710655, 562949953421311, 1125899906842623, 2251799813685247]

        #print('ans:')  
        #print(answer) 
    
    if int(math.log2(step)) >= deepth - 1:
        tmp_ans = deepth
        killed = tmp_list[deepth - 1]
    else:
        tmp_ans = int(math.log2(step)) 
        #print('tmp_ans')
        #print(tmp_ans)
        killed = tmp_list[tmp_ans]
        tmp_ans = tmp_ans + 1
        #print('killed:')
        #print(killed)
    if(total - killed) % step == 0:
        tmp_ans = tmp_ans + int((total - killed) / step)
    else:
        tmp_ans = tmp_ans + int((total - killed) / step) + 1
    
    print(tmp_ans)
        