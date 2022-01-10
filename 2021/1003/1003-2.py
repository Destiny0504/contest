times = input()
times = int(times)
for i in range(times):
    tmp1 = input()
    weapons, health = tmp1.split()
    health = int(health)
    weapons = input()
    weapons = list(weapons.split())
    for i in range(len(weapons)):
        weapons[i] = int(weapons[i])
    if len(weapons) > 1:
        attack1 = int(max(weapons))
        
        weapons.pop(weapons.index(attack1))
        #print(health)
        attack2 = attack1 + int(max(weapons))
        if health % attack2 == 0:
            print(2 * int(health / attack2))
        elif((health % attack2) > attack1):
            print(2 * int(health / attack2) + 2)
        else:
            print(2 * int(health / attack2) + 1)
    else:
        attack1 = int(weapons[0])
        if health % attack1 == 0:
            print(int(health / attack1))
        else:
            print(int(health / attack1) + 1)
