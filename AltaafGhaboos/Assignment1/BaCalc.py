# Program to perform basic calculator functions
# Variables are A for control, x and y to hold raw numbers and z to hold the result.
# Strings are B for control and calculation to calculate

# Declaring the variables
A=0
B="y"
x=0
y=0
z=0
calculator="yes"

# Defining the functions for the calculations to be carried out
def addition (): #function for addition
  z = int(x) +int(y)
  print("The answer is:", z)

def subtraction (): #function for subtraction
    z = int(x) - int(y)
    print("The answer is:", z)

def multiplication (): #function for multiplication
    z = int(x) * int(y)
    print ("The answer is:", z)

def division (): #function for division
    z = int(x) / int(y)
    print ("The answer is:", z)

# Start of the calculator
B = input("Do you want to perform a calculation? (yes/no) ") #asking the user if he/she wants to perform a calculation
print(B) #show the user answer

if B=="no":
    print("Thank you for your time")

# Performing calculator function
elif B=="yes":
    print("Would you like to perform an addition, subtraction, multiplication or division? ") #asking calculation type
    calculator = input()
    print(calculator)

    if calculator=="addition":
        x = input("Please input your first value: ")
        print(x)
        y = input("Please input your second value: ")
        print(y)
        addition()

    elif calculator=="subtraction":
        x = input("Please input your first value: ")
        print(x)
        y = input("Please input your second value: ")
        print(y)
        subtraction()

    elif calculator=="multiplication":
        x = input("Please input your first value: ")
        print(x)
        y = input("Please input your second value: ")
        print(y)
        multiplication()

    elif calculator=="division":
        x = input("Please input your first value: ")
        print(x)
        y = input("Please input your second value: ")
        print(y)
        division()

    else:
        print("Wrong input. Please restart the program")
else:
    print("Wrong input. Please restart the program")




