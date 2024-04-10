print ('\n****************Calculadora python V2*******************')

print ('\nSelecione o numero da operação desejada!')

print ('\n 1- Soma \n 2- Subtração \n 3- Multiplicação\n 4- Divisão')

operacao= input('\nDigite a sua opção (1, 2, 3, 4 ): ')
num1=float(input('\nDigite um Numero: '))
num2=float(input('\nDigite outro numero: '))


if operacao == '1':
    resultado= num1 + num2
    print ('\n',num1,'+', num2,)
elif operacao== '2':
    resultado= num1 - num2
    print ('\n',num1,'-', num2)
elif operacao== '3':
    resultado= num1 * num2
    print ('\n',num1,'*', num2)
elif operacao== '4':
    resultado= num1 / num2
    print ('\n',num1,'/', num2)

else: 
    print('\n', 'Operação Inválida') 


print('\n Resultado:',resultado)
