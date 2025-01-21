import sys
#integer
val1=10
print(val1)
print(type(val1))
print(sys.getsizeof(val1))
print(val1,'is Integer?',isinstance(val1,int))
#float
val2=93.2
print(val2)
print(type(val2))
print(sys.getsizeof(val2))
print(val2,'is float?',isinstance(val2,float))
#complex
val3=25+10j
print(val3)
print(type(val3))
print(sys.getsizeof(val3))
print(val3,'is float?',isinstance(val3,complex))
print(sys.getsizeof(int()))
print(sys.getsizeof(float()))
print(sys.getsizeof(complex()))
#boolean
bool1=True
bool2=False
print(type(bool1))
print(type(bool2))
print(isinstance(bool1,bool))
print(bool(0))
print(bool(1))
print(bool(7))
print(bool('7'))
print(bool(int))
print(bool(set))
print(bool(None))
print(bool(False))
#strings
#string creation
string='hi'
str1="var"
str2='''laxmi'''
str3="""amrutha"""
print(string,str1,str2,str3)
mystr=('Happy'
       ' Monday'
       ' Everyone')
print(mystr)
mul='\nIt\'s Monday!'
print(5*mul)
print(len(mul))
