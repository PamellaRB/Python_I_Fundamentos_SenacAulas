# 1 - Escreva  um código que verifique se um número fornecido é positivo, negativo ou zero.

num_int = int (input ("Digite um número: "))

if num_int % 2 == 0:
#Como o sinal de "%" se refere "ao resto da divisão", quando dividimos 2/2 = 1, sendo assim o sinal de "," é 0 (1,0)
#Porem, se uma divisão ocorrer em um numero impar 3/2 =  1,5, o sinal depois da "," é 5, sendo assim não é igual a 0
#A partir do resto da divisão "%" você consegue destinguir um numero entre par ou ímpar
    print("O número positivo")
elif num_int == 0:
    print("O número informado é 0!")
else: 
    print ("O número é negativo")

# 2 - Crie uma variável chamada `temperatura` e atribua a ela um valor numérico. 
# Depois, use as instruções `if`, `elif`, e `else` para decidir qual mensagem será exibida.
# - Se a temperatura for maior que 30, exiba "Está muito quente."
# - Se a temperatura for entre 20 e 30, exiba "O clima está agradável."
# - Se a temperatura for entre 10 e 19, exiba "Está um pouco frio."
# - Se a temperatura for menor que 10, exiba "Está muito frio."

temperatura = int (input("Informe a temperatura: "))

if temperatura <10:
    print("Esta muito frio!")
elif temperatura >=10 and temperatura <=19:
    print("Está um pouco frio")
elif temperatura >=20 and temperatura <=30:
    print("O clima está agradável!")
else:
    print("Esta muito quente!")

# 3- Crie uma variável chamada `nota` e atribua a ela um valor numérico entre 0 e 100. 
# Depois, use as instruções `if`, `elif`, e `else` para determinar o seu desempenho:
# - Se a nota for maior ou igual a 90, exiba "Excelente".
# - Se a nota for entre 70 e 89, exiba "Bom".
# - Se a nota for entre 50 e 69, exiba "Regular".
# - Se a nota for menor que 50, exiba "Insuficiente".

nota = float (input("Informe o valor da sua nota (0-100): "))

if nota >= 90:
    print("Nota Excelente!")
elif nota >= 70 and nota <= 89:
    print("Nota Boa!")
elif nota >= 50 and nota <=69:
    print("Nota Regular")
else:
    print("Nota Insuficiente!")