#https://atcoder.jp/contests/arc129/tasks/arc129_c
n = int(input())
#print(n)
now = 1
total = 1
ans = ''

while(n >= total):
    now += 1
    total += now
    ans += '7'

total -= now
for i in range(n - total):
    ans += '1281'
print(ans)