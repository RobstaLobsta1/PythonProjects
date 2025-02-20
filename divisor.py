#Exercise 4

'''Create a program that asks the user for a number and then prints 
out a list of all the divisors of that number. (If you dont know 
what a divisor is, it is a number that divides evenly into another 
number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

num = int(input("Enter a number : "))
#Define range of list, from 1 to the input number. +1 required to include the inputted number in list
listRange = list(range(1,num+1))

divisorList = []

for i in listRange:
    #For each number in the range, if the remainder is zero, then it is a divisor. Then add divisor to the list
    if num % i == 0:
         divisorList.append(i)

#Print list when done
print(divisorList)


