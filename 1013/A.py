times = input()

for i in range(int(times)):
    data = input()
    a, b, c = data.split()
    a = int(a)
    b = int(b)
    c = int(c)
    ans_a = a
    ans_b = b
    ans_c = c
    tmp = max(a, b, c)
    if tmp != a or max(b,c) == a:
        ans_a = tmp - a + 1
    else:
        ans_a = 0
    if tmp != b or max(a,c) == b:
        ans_b = tmp - b + 1
    else:
        ans_b = 0
    if tmp != c or max(b,a) == c:
        ans_c = tmp - c + 1
    else:
        ans_c = 0
    print(f'{ans_a} {ans_b} {ans_c}')