times = input()

for i in range(int(times)):
    data = input()
    a, b = data.split()
    print(str(-int(b)^2) + ' ' + str(int(a)^2))