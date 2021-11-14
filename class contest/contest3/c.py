

times = int(input())
dp = {}
key_list = range(times)
for t in key_list:    
    path_range = list(map(float, input().split()))
    path_range.insert(t, 0)

    for idx, v in enumerate(path_range):
        if idx != t:
            try:
                dp[t][idx] = v
            except:
                dp[t] = {}
                dp[t][idx] = v

dp2 = {}
for depth in range(times):
    if depth = 0: continue
    nextlist = list(set(key_list) - set([depth]))
    for d in dp:
        if (d[0] != depth):
            break
        for nxt in nextlist:
            d[nxt]
            
             

