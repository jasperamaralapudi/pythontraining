inp=int(input())
if inp<100 or inp>200:
    print('INVALID INPUT')
else:
    if inp%4==0:
        print(f"{inp//4}\n{inp//4}\n{inp//4}\n{inp//4}")
    else:
        o1=inp//4
        o2=inp//4
        o3=inp//4
        o4=inp-(o1+o2+o3) #or o+inp%4
        print(o1)
        print(o2)
        print(o3)
        print(o4)