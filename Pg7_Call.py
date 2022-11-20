def Factorial(num):
	if (num==1):
		return 1

	return num * Factorial(num-1)


print("Factorial of 5 is:", Factorial(5))
print("Factorial of 6 is:", Factorial(6))