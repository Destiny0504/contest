nothing = input()
tmp1 = input()
tmp2 = input()
a = list(tmp1.split())
b = list(tmp2.split())
for i in range(len(a)):
    a[i] = int(a[i])
    b[i] = int(b[i])
ans = b[0] - a[0] + 1
loss = 1
print(tmp1)
print(tmp2)

for i in range(int(nothing) - 1):
    ans = ans * (b[i + 1] - a[i + 1] + 1)
    loss = loss * (b[i] - a[i + 1])

print(ans)
print(loss)