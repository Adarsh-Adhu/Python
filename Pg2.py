"""Write a python script to accept an integer from the 
user and compute it's factorial. Display the output."""

num= int(input("Enter a number: "))
Factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, Factorial does not exist for negative numbers")
elif num == 0:
   print("The Factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       Factorial = Factorial*i
   print("The Factorial of",num,"is",Factorial)