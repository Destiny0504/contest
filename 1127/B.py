#https://atcoder.jp/contests/abc229/tasks/abc229_b

number1, number2 = input().split()

if len(number1) > len(number2) :
    for i in range(1, len(number2) + 1):
        if int(number2[-i]) + int(number1[-i]) > 9:
            print('Hard')
            exit()
else:
    for i in range(1, len(number1) + 1):
        if int(number2[-i]) + int(number1[-i]) > 9:
            print('Hard')
            exit()
print('Easy')