f=open('C:/Users/user/OneDrive/Desktop/PLACEMENT/PYTHON/binsearch.py','r')
print(f.read())
print(f.read(5))#prints first five characters of a file
print(f.readline())#prints the first line
print(f.readline())#twice to print two lines
#looping throught the file
for x in f:
    print(x)