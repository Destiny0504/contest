times = int(input())

for itr1 in range(times):
    data_len = int(input())
    data = list(map(lambda x : int(x),input().split()))
    min_value = min(data)
    max_value = max(data)
    print(max_value - min_value)