#Ask the user for a number. Depending on whether the number 
#is even or odd, print out an appropriate message to the user.

num1 = int(input("Enter a number : "))


#Essentially the modulus operator "%" divdes the two inputs and spits out
#the remainder of the operation. Example: 9 / 2 = 4 with a remainder of 1. 
#The number 1 serves as the solution to the modulus operation, and since 
#1 is NOT equal to 0, the conditional statement resolves to odd or "else"

#any number divisible by 2 is even
if num1 % 4 == 0:
    print("The number is a multiple of 4")
elif num1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

    '''
    For tomorrow ::: Add extras
    
    
    1. If the number is a multiple of 4, print out a different message.

    2. Ask the user for two numbers: one number to check (call it num) and 
    one number to divide by (check). If check divides evenly into num, 
    tell that to the user. If not, print a different appropriate message.
    
    '''




