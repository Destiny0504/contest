times = input()

for tmp in range(int(times)):
    data = input()
    n, k = data.split()
    n = int(n)
    k = int(k)
    coins = input()
    coins = coins.split()
    ans = []
    for i in range(n):
        coins[i] = int(coins[i])
        ans.append(0)

    i = 0
    while(i < n and k > 0):
        if i == 0:
            ans[0] = min(k ,10 ** (coins[1] -  coins[0]) - 1)
            if ans[0] == k:
                ans[0] += 1
            k -= ans[0] - 1         
        elif i == n - 1: 
            ans[i] = k
        elif i > 0 and i < n - 1:
            ans[i] = min(k ,10 ** (coins[i + 1] -  coins[i]) - 1)
            k -= ans[i]
        i += 1

    total = 0
    for itr in range(n):
        total += ((10 ** coins[itr]) * ans[itr])
    print(total)