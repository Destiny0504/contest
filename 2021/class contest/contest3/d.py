
def r(n):
    
    a,b,c = 1,2,7
    if n < 3:
        return [a,b,c][n]
    for i in range(n-2):
        a ,b, c = b, c, (c * 2 + b * 3 + a * 2)
    return c

print(r(int(input())))