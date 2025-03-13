import math

print("\n\nADVANCED CALCULATOR\n\n")
print("Operator List: \n")
print("~ Addition = +")
print("~ Subtraction = -")
print("~ Multiplication = *")
print("~ Division = /")
print("~ Exponentiation = **")
print("~ Remainder = %")
print("~ Square root = sqrt\n")


num1 = float(input("Enter 1st number: "))
ope = input("\nEnter the operator from the above list: ")
if(ope != "sqrt"):
  num2 = float(input("\nEnter 2nd number: "))


if (ope == "+"):
  print(f"\nANSWER = {num1 + num2}\n")
elif (ope == "-"):
  print(f"\nANSWER = {num1 - num2}\n")
elif (ope == "*"):
  print(f"\nANSWER = {num1 * num2}\n")
elif (ope == "/"):
  if num2 == 0:
    print("\nCan't divide by zero\n")
  else:
    print(f"\nANSWER = {num1 / num2}\n")
elif (ope == "**"):
  print(f"\nANSWER = {pow(num1,  num2)}\n")
elif (ope == "%"):
  print(f"\nANSWER = {num1 % num2}\n")
elif(ope == "sqrt"):
  print(f"\nANSWER = {math.sqrt(num1)}\n")
else:
  print("\nInvalid input!!\n")