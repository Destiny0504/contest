times = input()
tmp = input()

tmp = list(tmp.split())
data = []
plus = 0
minus = 0
ans = 0
for i in range(1,int(times)):
    data.append(abs(int(tmp[i]) - int(tmp[i - 1])))

minus = data[0]
ans = data[0]

for i in range(1, int(times) - 1):
    tp = data[i]
    plus = plus + tp    
    minus = minus - tp
    plus = max(tp,plus)
    tmp = plus
    plus = minus
    minus = tmp
    ans = max(plus,minus,ans)
print(ans)
