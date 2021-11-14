times = input()

for i in range(int(times)):
    length = input()
    data = input()
    left = 0 
    right = int(length) - 1
    ans_left = []
    ans_right = []
    
    while(left < right):
        if(data[right] == '1'):
            right -= 1
        if(data[left] == '0'):
            left += 1
    #print(ans_left)
    #print(list(reversed(ans_right)))
    if len(ans_left) == 0:
        print(0)
    else:
        print(1)
        print(str(len(ans_left) + len(ans_right)) + ' ' + ' '.join(ans_left + list(reversed(ans_right))))
    
            
