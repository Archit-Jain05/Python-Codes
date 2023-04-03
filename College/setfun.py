#in and len()
s1={'pen','pencil','marker'}
print('pen' in s1)
print('hello' in s1)
print(len(s1))

#set functions

s1={1,2,2,3,4,5,2}
s2={4,5,6,7,8}
s3={3,4}
s4={10,12}
print(s1|s2)

print(s1&s2)

print(s3<=s1)
print(s3>=s1)
print(s3.isdisjoint(s1))
print(s3.isdisjoint(s4))

