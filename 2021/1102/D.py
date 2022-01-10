times = input()

for itr1 in range(int(times)):
    nothing = input()
    number = input()
    color = input()
    number = number.split()
    max_b = 1
    cou_b = 0
    cou_r = 0
    min_r = int(nothing)
    ans = 'yes'
    for itr2 in range(len(color)):
        if color[itr2] == 'B':
            if int(number[itr2]) > max_b:
                max_b = int(number[itr2])
            if int(number[itr2]) == 1:
                cou_b += 1
        else:
            if int(number[itr2]) < min_r:
                min_r = int(number[itr2])
            if int(number[itr2]) == int(nothing):
                cou_r += 1
    
    if max_b < color.count('B') or cou_b > 1:
        ans = 'No'
    if int(nothing) - min_r < color.count('R') or cou_r > 1:
        ans = 'No'


    print(ans)