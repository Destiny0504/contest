times = input()
data = input()
data = list(data.split())
count = 0

ans = 0

sum_data = []

for i in range(int(times)):
    data[i] = int(data[i])

if min(data) > 0:
    print(0)
    exit()


tmp = int(times)
for i in range(int(times)):
    for j in range(i,int(times)):
        if i == 0:
            sum_data.append(sum(data[0:j + 1]))
        else:
            sum_data.append(sum_data[count - tmp + j] - data[i - 1])
            #print(count - tmp + j)
    
    count = count + j - i + 1
    #print(count)

#print(sum_data)
sum_data = list(filter(lambda x:x < 0, sum_data))

print(len(sum_data))