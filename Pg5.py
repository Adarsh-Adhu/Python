"""Write a menu driven python script to perform addition,
 subtraction, multiplication and division on two numbers."""

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

while(1):
	print("\nEnter the number of your choice of operation:\n\n1---> Add \n2---> Subtract \n3---> Multiply \n4---> Divide \n0---> Exit\n")
	choice = int(input())

	if choice == 0:
		break
	
	elif choice == 1:
		print(" SUM \n",x+y)

	elif choice == 2:
		print("SUBTRACTION \n",x-y)

	elif choice == 3:
		print("MULTIPLICATION \n",x*y)

	elif choice == 4:
		print("DIVIDE \n",x/y)