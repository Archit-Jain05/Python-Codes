print("Enter a string: ")
s1=input()

s2=s1.upper()
print(s2)


now=s1.split()

length=len(now)
print("Number of words = ",length)

for i in now:
    print(i)

print("Enter character to count: ")
s=input()
s=s[0]
count=s1.count(s)
print("The character '",s,"' appears",count,"times in the string.")
