n, x = input().split()
n = int(n)
x = int(x)

friend = input().split()
known = []
tmp = len(known)
known.append(int(x))
known.append(int(friend[x - 1]))
ans = len(known)

while(ans != tmp):
    tmp = ans
    if int(friend[known[-1] - 1]) not in known:
        known.append(int(friend[known[-1] - 1]))
    #print(known)
    ans = len(known)
print(ans)