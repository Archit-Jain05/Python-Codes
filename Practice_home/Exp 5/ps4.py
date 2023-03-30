my_string = "w3resource"
dict = {}

for char in my_string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)