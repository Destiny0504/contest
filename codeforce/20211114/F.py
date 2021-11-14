import copy
def LCS(data, length, curent):
    test = True
    tmp = []
    ans = ''
    max_len = 0
    for i in range(length):
        if curent[i] == -1:
            return ''
    for i in range(length - 1):
        if data[i][curent[i]] != data[i + 1][curent[i + 1]]:
            test = False
            break
    if test:
        char = data[i][curent[i]]
        for i in range(length):
            curent[i] -= 1
        return LCS(data, length, curent) + char
    else:
        for i in range(length):
            new_cur = copy.deepcopy(curent)
            new_cur[i] -= 1
            #print(new_cur)
            tmp.append(LCS(data, length, new_cur)) 
    for i in range(length):
        if len(ans) < len(tmp[i]):
            ans = tmp[i]
    return ans

times = input()
for itr in range(int(times)):
    data_len = input()
    data_len = int(data_len)
    data = []
    cur_list = []
    for itr2 in range(data_len):
        data.append(input())
        cur_list.append(len(data[itr2]) - 1)
    #print(cur_list)

    the_ans = LCS(data, data_len, cur_list)
    print(len(the_ans))
    print(the_ans)
