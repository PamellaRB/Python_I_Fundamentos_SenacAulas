#1- Crie um programa que peça ao usuário para digitar um número inteiro. O programa deve verificar se o número é par ou ímpar. 
# Se o número for par, exiba a mensagem "O número é par". Caso contrário, exiba "O número é ímpar".
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Seguindo a mesma linha do exercicio do documento 5. Este exercicio irá focar na continuidade caso o resultado for falso

num_int = int (input ("Digite um número inteiro: "))

if num_int % 2 == 0:
#Como o sinal de "%" se refere "ao resto da divisão", quando dividimos 2/2 = 1, sendo assim o sinal de "," é 0 (1,0)
#Porem, se uma divisão ocorrer em um numero impar 3/2 =  1,5, o sinal depois da "," é 5, sendo assim não é igual a 0
#A partir do resto da divisão "%" você consegue destinguir um numero entre par ou ímpar
    print("O número é par")
else: 
    print ("O número é ímpar")

#2 - Crie um programa que peça ao usuário para digitar sua idade. O programa deve verificar se o usuário é maior de idade 
# (18 anos ou mais). Se for, exiba a mensagem "Você é maior de idade". Caso contrário, exiba "Você é menor de idade".
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

idade = int (input("Informe sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
