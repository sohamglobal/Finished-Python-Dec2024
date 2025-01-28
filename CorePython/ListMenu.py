skills=[]
cho=None

while cho!=6:
    print("1. Add new skill ")
    print("2. List of skills ")
    print("3. Search a skill ")
    print("4. Remove a skill ")
    print("5. Clear list ")
    print("6. Exit ")
    cho=int(input("Enter choice : "))

    if cho==1:
        sk=input('Enter skill to add ')
        skills.append(sk)
    elif cho==2:
        print(skills)
    elif cho==3:
        sk=input('Enter skill to search ')
        if sk in skills:
            print('found')
        else:
            print('not found')
    elif cho==4:
        sk=input('Enter skill to remove ')
        skills.remove(sk)
    elif cho==5:
        skills.clear()
    elif cho==6:
        print('thanks...')
    else:
        print('invalid option')
