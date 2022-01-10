times = input()
times = int(times)
for i in range(times):
    tmp1 = input()
    weapons, health = tmp1.split()
    weapons = input()
    weapons = list(weapons.split())
    attack1 = int(max(weapons))
    weapons.pop(weapons.index(str(attack1)))
    health = int(health) - attack1
    #print(health)
    attack2 = attack1 + int(max(weapons))
    #print(attack2)
    if health % attack2 != 0 and health > attack2:
        if (health % attack2) > (attack2 - attack1):
            print(2 * (int(health / attack2)) + 3)
        else:
            print(2 * (int(health / attack2)) + 2)
    elif health > attack2:
        print(2 * (int(health / attack2)) + 1)
    elif health > 0:
        if health - attack2 + attack1 > 0 :
            print(3)
        else:
            print(2)
    else:
        print(1)
     
