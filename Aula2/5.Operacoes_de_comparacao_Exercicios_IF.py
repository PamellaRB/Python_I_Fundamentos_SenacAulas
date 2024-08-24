#1 - Crie um programa que peça ao usuário para digitar a sua idade e a idade de um amigo. 
# Verifique se as idades são iguais e, se forem, exiba a mensagem "Vocês têm a mesma idade".

idade1 = int (input ("Informe sua idade "))
idade2 = int (input ("intome a idade de um amigo "))

if idade1 == idade2:
    print("Suas idades são iguais!")


#2 - Crie um programa que peça ao usuário para digitar dois números. 
# Verifique se os números são diferentes e, se forem, exiba a mensagem "Os números são diferentes".

num1 = int (input("Insira um numero: "))
num2 = int (input ("Insira outro numero: "))

if num1 != num2:
    print("Os números inseridos são diferentes")

#3- Crie um programa que peça ao usuário para digitar a sua altura e a altura de um amigo (em centímetros). 
# Verifique se a altura do usuário é maior que a do amigo e, se for, exiba a mensagem "Você é mais alto que seu amigo".

alt1 = float (input ("Informe sua altura em cm: "))
alt2 = float (input ("Informa a altura de um amigo em cm: "))

if alt1 > alt2:
    print("Você é mais alto que seu amigo")

#4-  Crie um programa que peça ao usuário para digitar a sua nota em uma prova e a nota mínima necessária para passar. 
# Verifique se a nota do usuário é menor que a nota mínima e, se for, exiba a mensagem "Você não passou na prova"

nota_prova = int (input("Qual sua nota na prova? "))
nota_minima = int (input("Qual a nota mínima para passar? "))

if nota_prova < nota_minima:
    print ("Você não passou na prova")

#Dica de atalho:
#Shift + Alt + Seta p/ Baixo = Copia a linha da qual o cursor esta para baixo
#A continuidade do if (se) para continuar a aplicação apresentada acima será else (se não), para poder aplicar uma condição simples
#completando com a resposta caso ela for falsa. Documento 6.
