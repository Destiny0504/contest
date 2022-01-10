# https://atcoder.jp/contests/abc228/tasks/abc228_a
s, t, x = input().split()
s = int(s)
t = int(t)
x = int(x)

if t < s :
    t += 24
    if x < s :
        x += 24
    if x >= s and x < t:
        print('Yes')
    else:
        print('No')
else:
    if x >= s and x < t:
        print('Yes')
    else:
        print('No')