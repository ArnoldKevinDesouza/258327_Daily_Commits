#replace second,third,... occurance of first character with dollar

word=input()
lis=list(word)
#print(lis)
letter=lis[0].lower()
for i in range(1, len(word)):
    if(letter == lis[i]):
        lis[i] = "$"
str1=" "
print (str1.join(lis))
