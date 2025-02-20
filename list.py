#Exercise 3

#Write a program that prints out all the elements of the list that are less than 5

'''
Lists are appendable and you can iterate through them using loops. Elements can be either numerical or strings. 

Exercise Extras


    1. Instead of printing the elements one by one, make a new list 
    that has all the elements less than 5 from this list in it and 
    print out this new list.

    2. Write this in one line of Python.

    3. Ask the user for a number and return a list that contains only 
    elements from the original list a that are smaller than that 
    number given by the user.

'''


#Define list
list = [1,1,2,3,5,13,21,34,55,89]

#Loop through list, and print out each element that is less than 5
for i in list:
    if i < 5:
        print(i)
