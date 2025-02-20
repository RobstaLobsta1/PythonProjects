#Exercise 3

#Write a program that prints out all the elements of the list that are less than 5

'''
Lists are appendable and you can iterate through them using loops. Elements can be either numerical or strings. 

'''


#Define list
list = [1,1,2,3,5,13,21,34,55,89]

#Loop through list, and print out each element that is less than 5
for i in list:
    if i < 5:
        print(i)
