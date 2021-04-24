#Write aprogram to check use input abbrevation.
#If the user enters "lol", print "lauhing out loud".
#If the user enters "rofl", print "rolling on the floor lauhing".
#If the user enters "lmk", print "let me know".
#If the user enters "smh", print "shaking my head".

st=input("Enter an abbrevation(from among : lol, rofl, lmk or smh) to know the full form : \n")

if(st == "lol"):
    print("laughing out loud")

elif(st == "rofl"):
    print("rolling on the floor laughing")
    
elif(st == "lmk"):
    print("let me know")
    
elif(st == "smh"):
    print("shaking my head")

else:
    print("Invalid choice!")