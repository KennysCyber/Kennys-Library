import math

#Calculator Project Update 11/02/2024

#User Selection of Operation
print("Select an operation to perform:")
print("1- ADD")
print("2- SUBTRACT")
print("3- MULTIPLY")
print("4- DIVIDE")
print("5- SQUARE ROOT")
print("6- RAISE TO POWER")


#Declare what operation ingest.
operation = input()

#Specifiy what operation does. (actual computation)
if operation == "1": #perform addtions
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Sum is  " + str(int(num1) + int(num2)))
elif operation == "2": #perform subtraction
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Differnce is  " + str(int(num1) - int(num2)))
elif operation == "3": #perform multipication
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Product is  " + str(int(num1) * int(num2)))
elif operation == "4": #perform division
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Result is  " + str(int(num1) / int(num2)))
elif operation == "5": #perform Square root
    num = int(input("Enter Number: "))
    print("The Square root is %f " %(math.sqrt(num)))
elif operation == "6": #perform exponent raise
    num = int(input("Enter Number: "))
    print("The Result is %d " %(pow(num, 2)))
else:
    print("Invalid Entry")
