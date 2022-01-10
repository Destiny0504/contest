times = input()
data = 0.0
tmp = input()
tmp = tmp.split()
for i in range(int(times)):
    tmp[i] = float(tmp[i])

for i in tmp:
    if i > 0.0:
        data = data + i
ans = data / float(times)
ans_tmp1 = int(data / float(times))

if ans - ans_tmp1 < 1e-7:
    ans = ans_tmp1
    print(ans)
else:
    print(str(ans)[:3])

