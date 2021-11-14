itr = input()
itr = int(itr)
for i in range(itr):
    tmp = input()
    ans = 1
    tmp = 2 * int(tmp) + 1
    for j in range(tmp):
        if j > 2:
            ans = (ans * j) % 1000000007
    print(ans)