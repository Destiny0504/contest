nothing = input()
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

A = input()
B = input()
C = input()

A = ''.join(filter(lambda a: a != '?',A))
B = ''.join(filter(lambda a: a != '?',B))
C = ''.join(filter(lambda a: a != '?',C))
ans = 0
for i in range(len(A)):
    for j in range(len(A)):
        tmpA = A[:j] + A[j+i:]  
        D = longest_common_sequence(A,B,len(A),len(B))
        tmp_ans = len(longest_common_sequence(D,C,len(D),len(C)))
        if tmp_ans > ans:
            ans = tmp_ans


print(3 * (ans))

