#Grabbing user input and outputting after saving to var
name = input("Enter your name: ")

age = input("Enter your age: ")

#Calculates what year the user will be 100 years old. 
#Hard coded although and will need to be updated yOy
modAge = 2024 + (100 -int(age))

print("Hello, " + name + "! You are " + str(age) + " years old.")
print("You are going to turn 100 in the year " + str(modAge))