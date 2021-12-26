import math 
import string 
import re
 
idade = -20 
media = 14.23

# abs
print(abs(idade))

#round

print(round(media))

"""
%s
%d
%o
%x
%f
%%
%e
"""
print("Your age  %d "%(abs(idade)))

name = "Pedro"

print(name[-1:0:-1])
#ascii_letters
print(string.ascii_letters)
print(10 // 3)
print('.'*50)

fruits = ['banana','apple','oniom']
"""
append()
sort()
remove()
reverse()
pop()
"""
fruits.append('quiwi')
for i,fruit in enumerate(fruits):
    print(f' {1+i} => {fruit}')

names = ('Pedro','Zau','Marco','José')
print(names[0])
loja = tuple(fruits)
print(loja)
registre = list(names)
print(registre)

s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))
print(s1,s2,s3)
s1s2 = s1.union(s2)
print(s1s2)
print(s1s2.difference(s3))

url = "https//:facebook.com"

change = re.compile(r'https')

print(re.sub('https//:','',url))
print(re.findall('https',url))
print(re.search('.com',url))


def fatorial(num):
    if num <= 1:
        return 1
    else:
        return num*fatorial(num-1)


print(fatorial(5))


