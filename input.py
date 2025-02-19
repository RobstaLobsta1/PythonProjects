#Exercise 1

#Grabbing user input and outputting after saving to var
name = input("Enter your name: ")

#Need to add function to ensure user input is only an integer and not a string or float
age = int(input("Enter your age: "))

#Calculates what year the user will be 100 years old. 
#Hard coded although and will need to be updated yOy
modAge = 2024 + (100 - age)

print("Hello, " + name + "! You are " + str(age) + " years old.")
#Concatenation Practice
#Able to print out message multiple times by doing...
#"Multiplication with Strings"
print(4 * ("\nYou are going to turn 100 in the year " + str(modAge)))