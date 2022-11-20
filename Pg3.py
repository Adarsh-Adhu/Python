"""Write a python script to accept an integer from the user and
 reverse it using loop iterations."""

N =int(input("Enter the Number:"))
 
# using reversed() to perform the back iteration
print ("The reversed numbers are : ", end = "")
for num in reversed(range(N + 1)) :
    print(num, end = " ")