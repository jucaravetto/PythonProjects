print("Saudações! Esta é sua calculadora feita em Python!\n")

num1 = int(input('Entre com seu primeiro número: '))
num2 = int(input('Entre com seu segundo número: '))

#teste comentário
#to usando o seguinte site pra aprender:
#https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

#Este site tem uma versão de calculadoras com funções
#https://www.programiz.com/python-programming/examples/calculator

#Primeiro jeito que fiz, agora testar nova formatação
#print("\nA soma é:")   
#print(num1+num2,"\n")

# Addition
print('{} + {} = '.format(num1, num2),num1 + num2) #exibe o resultado logo depois de calcular a soma
#print(num1 + num2)

# Subtraction
print('{} - {} = '.format(num1, num2),num1 - num2)
#print(num1 - num2)

# Multiplication
print('{} * {} = '.format(num1, num2),num1 * num2)
#print(num1 * num2)

# Division
print('{} / {} = '.format(num1, num2),num1 / num2)
#print(num1 / num2)