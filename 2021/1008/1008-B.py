times = input()
for i in range(int(times)):
        ans = 0
        data = input()
        n, k = data.split()
        n = int(n)
        k = list(bin(int(k)))
        k = k[2:]
        #print(k)
        tmp = len(k)
        for i in range(tmp):
            if k[i] == '1':
                #print(i)
                ans = ans + n ** (tmp - i - 1)
        print(ans % 1000000007)
