times = input()

for itr in range(int(times)):
    data = input()
    row, column = data.split()
    row = int(row)
    column = int(column)
    ans = 0
    if row >= 3:
        ans += (row // 3) * column
        row = row % 3
    if column >= 3:
        ans += (column // 3) * row
        column = column % 3

    if column == 2 and row == 2 :
        ans += 2
    elif (column == 2 and row == 1) or (column == 1 and row == 2):
        ans += 1
    if (column == 1 and row == 1) :
        ans += 1
    print(ans)