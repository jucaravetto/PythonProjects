operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division

''')
#Fonte
#https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

#PRÓXIMOS PASSOS: DEFINIR AS FUNÇÕES PRA CALCULADORA E FUNÇÃO UTILIZAR DE NOVO.


if operation == '+':
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    print('{} + {} = '.format(num1, num2),num1 + num2)
    #print(num1 + num2)
    

elif operation == '-':
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    print('{} - {} = '.format(num1, num2),num1 - num2)
    #print(num1 - num2)

elif operation == '*':
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    print('{} * {} = '.format(num1, num2),num1 * num2)
    #print(num1 * num2)

elif operation == '/':
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    print('{} / {} = '.format(num1, num2),num1 / num2)
    #print(num1 / num2)

else:
    print('Você digitou um operador incorreto; por favor, tente outra vez.\n\n')