#Create a dictionary to store details of a person.
#The dictionary should contain name, address, gender, age and telephone number as keys.
#Display only Name and Telephone number.
print("Enter the details:\n")
Person = {}

print("Enter the name of the person:")
Name = input()
Person["Name"] = Name

Address = input("Enter the address of the person: \n")
Person["Address"] = Address

Gender = input("Enter the gender of the person: \n")
Person["Gender"] = Gender

Age = int(input("Enter the age of the person: \n"))
Person["Age"] = Age

Telephone = int(input("Enter the telephone number of the person: \n"))
Person["Telephone"] = Telephone

print("Name:", Person["Name"],"\nTelephone:", Person["Telephone"])