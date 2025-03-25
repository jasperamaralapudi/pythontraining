p=int(input('Enter number 1: '))
q=int(input('Enter number 2: '))
r=int(input('Enter number 3: '))
l=[p,q,r]
l=sorted(l)
count=0
while l[0]!=l[1] or l[0]!=l[2]:
    if l[0]+1==l[1] and l[1]+1==l[2]:
        count=-1
        break
    l[0]+=1
    l[1]+=1
    l[2]-=1
    count+=1
    l=sorted(l)
print('Minimum operations:',count)