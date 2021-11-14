times = input()
data = 0.0
ans_tmp2 = 0.0
tmp = input()
tmp = tmp.split()
for i in range(int(times)):
    tmp[i] = float(tmp[i])

a = max(tmp)

for i in range(len(tmp) - 1):
    if tmp[i] != -1 and tmp[i + 1] != -1:
        tmp_ans = abs(tmp[i] - tmp[i + 1])
        if tmp_ans > ans_tmp2:
            ans_tmp2 = tmp_ans
        
if min(tmp) >= 0.0:
    ans = a - min(tmp)
    ans_tmp1 = int(ans)
    if ans - ans_tmp1 < 1e-8:
        ans = ans_tmp1
        print(ans)
    else:
        print(round(ans, 1))
    exit()

b = list(filter(lambda x:x >= 0, tmp))

if len(b) == 0:
    print(0)
    exit()

b = min(b)

ans = ((a - b) / 2)
ans_tmp1 = int(((a - b) / 2))
if ans_tmp2 > ans:
    if ans - ans_tmp1 < 1e-7:
        print(int(ans_tmp2))
    else:
        print(ans_tmp2)
else:
    if ans - ans_tmp1 < 1e-7:
        ans = ans_tmp1
        print(ans)
    elif a == min(tmp):
        print(0)
    else:
        print(round(ans, 1))



