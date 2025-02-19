#Ask the user for a number. Depending on whether the number 
#is even or odd, print out an appropriate message to the user.




#Essentially the modulus operator "%" divdes the two inputs and spits out
#the remainder of the operation. Example: 9 / 2 = 4 with a remainder of 1. 
#The number 1 serves as the solution to the modulus operation, and since 
#1 is NOT equal to 0, the conditional statement resolves to odd or "else"
num1 = 0

while True:
    num1 = input("Enter a number : ")

    if num1 == "end":
        print("Goodbye")
        break
    elif int(num1) % 4 == 0:
        print("The number is a multiple of 4")
    elif int(num1) % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")