import sys
st=input()
letters=list(st)
min=len(st)
for i in range(0,len(st)-1):
    for j in range(1,len(st)):
        if letters[i]==letters[j]:
            if(min>j):
                min=j
                print(letters[min])
                sys.exit()

