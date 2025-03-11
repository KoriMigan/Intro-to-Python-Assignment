# Basic calculator program

#Get the user input
num1= float(input("Input the first number: "))
num2= float(input("Input the second number: "))
operation= input("Input the operation (+, -, *, /): ")

#Run operation to perform the calculations
if operation == "+":
    result= num1+num2
    print(f"{num1}+{num2}={result}")
elif operation == "-":
    result= num1-num2
    print(f"{num1}-{num2}={result}")
elif operation == "*":
    result= num1*num2
    print(f"{num1}*{num2}={result}")
elif operation == "/":
    if num2 !=0:
        result= num1/num2
        print(f"{num1}/{num2}= {result}")
    else:
        print("Error: Division by zero is not allowed for this operation.")
else:
    print("Invalid operation! Please enter an operaton +, -, * or /.")

