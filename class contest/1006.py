times = input()
times, money = times.split()
money = int(money)
cp = []
delicious = []
cost = []
answer = 0.0
for i in range(int(times)):
    data = input()
    d, c = data.split()
    delicious.append(int(d))
    cost.append(int(c))
    cp.append(int(d) / int(c))
#print(max(cp))

while(money > 0):
    if len(cp) == 0:
        break
    tmp = cp.index(max(cp))
    #print(tmp)
    
    if money >= cost[tmp]:
        money = money - cost[tmp]
        answer = answer + delicious[tmp]
    else:
        answer = answer + money * cp[tmp]
        money = 0
    cp.pop(tmp)
    cost.pop(tmp)
    delicious.pop(tmp)
print(answer)