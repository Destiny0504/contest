times = input()
for itr in range(int(times)):
    nothing = input()
    data = input()
    l = 0
    r = len(data) - 1 
    rm_char = ''
    ans = 0
    while(l < r):
        if data[l] == data[r]:
            l = l + 1
            r = r - 1
        else:
            l = l + 1
            r = r - 1
            if data[r] == rm_char:
                rm_char = ''
                ans = ans + 1
                continue
            rm_char = data[l]
    print(ans)

