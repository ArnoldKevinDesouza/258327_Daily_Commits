#Write a python code that asks a user how many pizza slices they want
#The pizzeria charges Rs. 123.00 a slice
#if user orders even number of slices, price per slice is Rs. 120.00
#Print the total price depending on how many slices user orders

slices=input("Enter how many pizza slices you want : \n")

if type(slices)!=int:
    print("Enter a number!")

elif(slices==0):
    print("Your bill is : Rs. 0")

elif(slices%2==0):
    bill=slices*(120.00)
    print("Your bill is : Rs. " + str(bill))

elif(slices%2!=0):
    bill=slices*(123.00)
    print("Your bill is : Rs. " + str(bill))

else:
    print("Wrong input!")