# https://atcoder.jp/contests/abc229/tasks/abc229_a
S1 = input()
S2 = input()
for i in range(len(S1) - 1):
    if S1[i] == '#':
        if i > 0:
            if S1[i + 1] == '.' and S2[i] == '.' and S1[i - 1] == '.':
                print('No')
                exit()
        else :
            if S1[i + 1] == '.' and S2[i] == '.':
                print('No')
                exit()
    else:
        if i > 0:
            if S1[i + 1] == '#' and S2[i] == '#' and S1[i - 1] == '#':
                print('No')
                exit()
        else :
            if S1[i + 1] == '#' and S2[i] == '#':
                print('No')
                exit()
print('Yes')