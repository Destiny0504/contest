n, x = input().split()
n = int(n)
x = int(x)

friend = input().split()
tmp = -1
known = x
ans = 0

while(ans != tmp):
    tmp = ans
    if int(friend[known - 1]) != -1 :
        tmp_know = int(friend[known - 1])
        friend[known - 1] = -1
        known = tmp_know
        ans += 1
    #print(known)

print(ans)