# https://atcoder.jp/contests/abc228/tasks/abc228_e
n, k, m  = input().split()
n = int(n)
k = int(k)
m = int(m)
print(((n**k)**m) % 998244353)