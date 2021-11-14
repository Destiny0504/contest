tmp = input()
n, m = tmp.split()
n = int(n)
m = int(m) 
tmp1 = n + m - 1
ans = 1
div = 1
for i in range(m):
    ans = ans * (tmp1 - i)
    div = div * (i + 1)


print(int(ans // div)) # important (if you need to divide a big interger -> output is a interger)
print(int(ans / div)) # this one will output a float number, so it will face the overflow problem