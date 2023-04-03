#string functions

str1='hello world'
str2='HELLO WORLD'
str3='Hello World'
str4='   hello world'
str5='Hi hello bye bellow'
print(len(str1))

print(str1.capitalize())

print(str2.casefold())
print(str2.lower())

print(str3.swapcase())
print(str1.title())

print(str2.casefold())

print(str1.replace('hello','hi'))
print(str4.strip())

print(str2.count('HELLO'))
print(str2.find('HELLo'))

print(str2.rindex('R'))

print(str5.partition('bye'))

print(str5.split(''))