#https://atcoder.jp/contests/abc229/tasks/abc229_c
N, W = input().split()
data = {}
delicious = []
for itr in range(int(N)):
    happy, cheese = input().split()
    delicious.append(int(happy))
    data[happy] = int(cheese)

delicious = sorted(delicious, reverse=True)

W = int(W)
itr = 0
ans = 0
while(W > 0 and itr < len(delicious)):
    if W > data[str(delicious[itr])] : 
        W -= data[str(delicious[itr])]
        ans += data[str(delicious[itr])] * delicious[itr]
    else: 
        ans += W * delicious[itr]
        W = 0
    itr += 1
print(ans)