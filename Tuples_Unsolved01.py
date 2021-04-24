# Write a python program to find the repeated items of a tuple

tuplex=(1,2,3,3,1,4)
print("Repeated items are : ")
for i in tuplex:
    if tuplex.count(i) > 1:
        print(i)