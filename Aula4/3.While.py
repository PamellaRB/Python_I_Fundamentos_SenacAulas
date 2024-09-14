#While = Enquanto

print("---ENQUANTO O CONTADOR FOR MENOR OU IGUAL A 5, A CONTAGEM IRÁ SE REPETIR---")
contador = 1
#Enquanto o contador for menor ou igual a 5 o bloco de codigo se repetira
while contador <5:
    print("Contagem ", contador)
    contador += 1

print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

print("---------USUÁRIO ADIVINHAR UM NÚMERO SECRETO, DECLARADO NA VARIAVEL--------")
numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe um número entre 1 até 10: "))

print("Parabéns, você acertou!")
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

print("-----------LOOP INFINITO - ESTA COMENTADO PARA NÃO COMER MEMORIA-----------")
print("x = 10")
print("while x > 5:")
print("         print(""Isso é um loop infinito)""")    

print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#Crie um código que soma números fornecidos pelo usuário até que a soma alcence o resultado de 100
soma = 0

while soma <100:
    #<100, pois se colocar <=100 irá pedir ao usuário que inclua mais números
    numero = int(input("Digite um número para soma: "))
    soma += numero
    print("Soma Atual: ", soma)
print("-----------------------A soma atingiu o limite de 100----------------------")