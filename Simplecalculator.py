num1 = int(input("Enter first number: "))
operator = input()
num2 = int(input("Enter second number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)   
elif operator == '%':
     print(num1 % num2)
elif operator == '//':
    print(num1 // num2) 
elif operator == '**':
    print(num1 ** num2)
