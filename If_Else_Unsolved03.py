#Write a python program to check the type of input(real,float,string,complex,zero)

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

def check_int(potential_float):
    try:
        int(potential_float)
        return True
    except ValueError:
        return False

value=input("Enter a number : ")

if(check_int(value)):
    if(int(value)==0):
        print("Zero and Real")
    else:
        print("Real")

else:
    if(check_float(value)):
        print("Float and Real")

    else:
        print("Complex")