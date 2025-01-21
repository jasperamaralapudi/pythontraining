'''
str1='hello'
str1[0:5]='holaa'
#del
del str1
print(str1)
'''
#concat
str1='jasper'
str2='enoch'
print(str1+' '+str2)
#iterating through a string
mystr='Hello Everyone'
for char in mystr:
    print(char,end=' ')
    print(type(char))
for char in enumerate(mystr):
    print(char)
    print(*char)
#string membership
print('Hello' in mystr)
print('Hi' in mystr)
print('Hello' not in mystr)
print('Hi' not in mystr)
#string partitioning
'''
The partition() method searches for a specified
string and splits the string into
-The first element contains the part before the argument string
-The second element contains the argument string.
-The third element contains the part after the argument string
'''
str5='Natural language processing with Python and R and Java'
L=str5.partition('and')
print(L)
#l1=str5.lpartition('and')
#print(l1) #attribute error
R=str5.rpartition('and')
print(R)
#string functions
mystr2='   Hello Everyone   '
print(mystr2)
print(mystr2.strip())
print(mystr2.lstrip()) 
print(mystr2.rstrip())
mystr3='***Hello Everyone***'
print(mystr3)
print(mystr3.strip('*'))
print(mystr3.lstrip('*'))
print(mystr3.rstrip('*'))