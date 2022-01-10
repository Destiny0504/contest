# https://codeforces.com/contest/1612/problem/B
# didn't solve
times = int(input())

for i in range(times):
    n, l, r = input().split()
    #print(n + ' ' + l + ' ' + r)
    n = int(n)
    l = int(l)
    r = int(r)
    if l > (n//2 + 1) or r < n//2:
        print(-1)
        continue
    else:
        ans = []
        another = False
        for i in range(n//2 - 1):
            if n - i != r:
                ans.append(str(n - i))
            else:
                another = True
        if another:
            ans.append(str(n - i - 1))
        if l == n - i - 1 and another:
            ans.append(str(l - 1))
        else :
            ans.append(str(l))
        #print(ans)
        another = False
        for i in range(n//2 - 1):
            if i + 1 != l:
                ans.append(str(i + 1))
            else :
                another = True
        if another:
            ans.append(str(i + 2))
        ans.append(str(r))
        if ans.count(str(l)) == 2 or ans.count(str(r)) == 2:
            print(-1)
        #print(ans)
        else:
            print(' '.join(ans))
        
