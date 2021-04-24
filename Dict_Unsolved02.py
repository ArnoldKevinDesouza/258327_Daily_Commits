# Write a Python program to convert a list into a nested dictionary of keys

list = [1, 2, 3, 4]
dictionary = current = {}
for name in list:
    current[name] = {}
    current = current[name]
print(dictionary)