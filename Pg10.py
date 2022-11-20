"""Write a Python script to prompt the user to enter two 
numbers through the keyboard and perform addition, 
subtraction, multiplication, division, modulus, floor 
division and exponential operation. Store the result of 
each operation in a different variable and display the result."""
A = int(input("Enter 1st Number:"))
B = int(input("Enter 2nd Number:"))

#Addition 
Sum = A + B
print("Sum of two given Number is :\n",Sum)

#Subtraction
Sub = A - B
print("Subtraction of two given Number is :\n",Sub)

#Multiplication 
Mul = A*B
print("MultiplicationM of two given Number is :\n",Mul)

#Division
Div = A/B
print("Division of two given Number is :\n",Div)

#Modulous
Mod = A % B
print("Modulous of two given Number is :\n",Mod)

#Floor division
F_Div = A // B
print("Floor Division of two given Number is :\n",F_Div)

#Exponential 
Expo = A ** B
print("Exponential of two given Number is :\n",Expo)