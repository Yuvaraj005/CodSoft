def add(n1, n2):
    return n1 + n2
 
def subtract(n1, n2):
    return n1 - n2
 
def multiply(n1, n2):
    return n1 * n2
 
def divide(n1, n2):
    return n1 / n2

exit = False
print("---------------------------") 
print("\tCALCULATOR") 
print("---------------------------") 

while exit!=True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    optn = int(input("Please select operation: "))

    if optn == 1:
        Val1 = int(input("Enter first number: "))
        Val2 = int(input("Enter second number: "))
        print("\n",Val1, "+", Val2, "=", add(Val1, Val2),"\n")
    
    elif optn == 2:
        Val1 = int(input("Enter first number: "))
        Val2 = int(input("Enter second number: "))
        print("\n",Val1, "-", Val2, "=", subtract(Val1, Val2),"\n")
    
    elif optn == 3:
        Val1 = int(input("Enter first number: "))
        Val2 = int(input("Enter second number: "))
        print("\n",Val1, "*", Val2, "=", multiply(Val1, Val2),"\n")
    
    elif optn == 4:
        Val1 = int(input("Enter first number: "))
        Val2 = int(input("Enter second number: "))
        print("\n",Val1, "/", Val2, "=", divide(Val1, Val2),"\n")
    elif optn == 5:
        print("Exiting...")
        exit = True
    else:
        print("\nInvalid input")