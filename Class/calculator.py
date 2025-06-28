number1 = input('Enter the first number: ')
num1 = int(number1)

sign = input('Enter the operation (+, -, *, /): ')

number2 = input('Enter the second number: ')
num2 = int(number2)

if sign == '+':
    print('Your result is ' + str(num1 + num2))
elif sign == '-':
    print('Your result is ' + str(num1 - num2))
elif sign == '*':
    print('Your result is ' + str(num1 * num2))
elif sign == '/':
    if num2 != 0:
        print('Your result is ' + str(num1 / num2))
    else:
        print('Error: Division by zero')
else:
    print('Please enter a valid operation: +, -, * or /')
