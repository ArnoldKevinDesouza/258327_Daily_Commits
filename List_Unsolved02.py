#Write a python program to change the position of every nth value with the (n+1)th value in the list

data = [10, 20, 30, 40]

print("Original list : ", data)

i = 0
while i < data.__len__() - 1:
    t = data[i]
    data[i] = data[i + 1]
    data[i + 1] = t
    i = i + 2

print("List after changing positions : ", data)