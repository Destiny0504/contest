def longest_common_sequence(string_x, string_y, len_x, len_y):
    if(len_x == 0 or len_y == 0):
        return ''
    elif(string_x[len_x - 1] == string_y[len_y - 1]):
        return longest_common_sequence(string_x, string_y, len_x-1, len_y-1) + string_x[len_x - 1]
    else:
        tmp1 = longest_common_sequence(string_x, string_y, len_x, len_y-1)
        tmp2 = longest_common_sequence(string_x, string_y, len_x-1, len_y)
        if len(tmp1) > len(tmp2):
            return tmp1
        else:
            return tmp2

times = input()
for itr in range(int(times)):
    