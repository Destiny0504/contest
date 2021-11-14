times = input()

for i in range(int(times)):
    data = input()
    n, k = data.split()
    n = int(n)
    k = int(k)
    tmp = 1
    cur = 1
    ans = 0
    if k == 1:
        print(n-1)
        continue
    while(cur < n):
        tmp = min(cur,k)
        if tmp < k :
            cur += tmp
            ans += 1
        else:
            if (n - cur ) % k == 0:
                ans += ((n - cur ) // k )
                #print((n - cur ) // k )
                break
            else :
                ans += ((n - cur ) // k ) + 1
                #print(((n - cur ) // k ) + 1)
                break

    #print('finished')
    print(ans)