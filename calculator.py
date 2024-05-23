import math

def functionname(numberone,numbertwo,operator):
    result = 0
    if operator == "add":
        result = numberone + numbertwo
    elif operator == "subtract": 
        ##todo: make this do stuff
        result = numberone  - numbertwo
    elif operator == "multiply":
        result = numberone * numbertwo
        ##todo: give this functionality 
    elif operator == "divide":
        print("stop trying to divide by zero")
        result = numberone / numbertwo
        #todo: add functionality
    else:
        print("invalid choice")

    return result


numberOne = float(input('type number '))
operator = input('what do you want to do with this ')
numberTwo = float(input('type number to do stuff with')) 

print(functionname(numberOne, numberTwo, operator))
