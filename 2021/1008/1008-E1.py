data = input()
data = int(data)
if data == 1:
    print(6)
else :
    ans =(2 ** (((2 ** (data + 1)) - 4 ) % 1000000007))
    print((6 * ans) % 1000000007)
