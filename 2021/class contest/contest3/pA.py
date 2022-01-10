times = input()
family = {}
for itr in range(int(times)):
    event = input()
    event = event.split() 
    #print(event)
    if event[0] == 'IN':
        if event[1] in family:
            family[event[1]].append(event[2])
        else:
            family[event[1]] = [event[2]]
    else:
        if event[1] in family:
            print(event[1] + ' ' + ' '.join(sorted(family[event[1]])))
            family[event[1]] = []
        else:
            print('CALL THE POLICE')

    #print(person)