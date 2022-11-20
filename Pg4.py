"""Write a python script to accept a string from the user and
 reverse it without using standard library functions."""
String=input("Enter String: ")
my_string=String
str=""
for i in my_string:
	str=i+str
print("Reversed string:",str)