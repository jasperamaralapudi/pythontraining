inp=int(input())
if inp>30 and inp<50:
    print('average')
if inp>=51 and inp<=60:
    print('good')
if inp>=61 and inp<=80:
    print('excellent')
if inp>=81 and inp<=100:
    print('outstanding')
if inp<30 and inp>100:
    print('Invalid input')