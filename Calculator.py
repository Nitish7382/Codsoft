def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def rem(a,b):
    return a%b

firstNum = int(input ("Enter the first number: "))
operator = input("Select operator between (+,-,*,/,%): ")
secondNum = int(input("Enter the second number: "))

if operator == "+":
    result=add(firstNum,secondNum)
    print(f"The sum of {firstNum} & {secondNum} is:{result}")

elif operator == "-":
    result= sub(firstNum,secondNum)
    print(f"The Substraction of {firstNum} & {secondNum} is: {result}")

elif operator == "*":
    result = mul(firstNum,secondNum)
    print(f"The Multiplication of {firstNum} & {secondNum} is: {result}")

elif operator == "/":
    result = div(firstNum,secondNum)
    print(f"The Division of {firstNum} & {secondNum} is: {result}")

elif operator == "%":
    result =rem(firstNum,secondNum)
    print(f"The Remainder of {firstNum} & {secondNum} is: {result}")

else:
    print("Invalid operator")