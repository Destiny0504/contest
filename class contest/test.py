tmp = 1
div = 1

for i in range(18):
    tmp = tmp * (i + 765)

for i in range(18):
    div = div * (i + 1)

print((tmp / div) % 1000000007)