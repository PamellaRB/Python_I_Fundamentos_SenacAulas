#1 - Escreva um código que percorra uma lista de números e encontre o primeiro número negativo. 
# Quando o número for encontrado, o loop deve parar.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

numeros = [1,5,98,5,62,4,5,3,45,-1,-8,8]

for numero in numeros: 
    if numero <0:
        print("O numero, ", numero, "é menor que zero!")
        break
print("Números da lista: ",numeros)

print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#2 - Escreva  um código que some apenas os números positivos de uma lista. 
# Se o número for negativo, o loop deve ignorá-lo e continuar.

numeros = [1,5,98,5,62,4,5,3,45,-1,-8,8]
soma = 0

for numero in numeros:
    if numero < 0:
        continue
    soma += numero
print("A soma da listagem de números é: ", soma)

print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#3 - Escreva um código que percorra uma lista de números e pare de executar assim que encontrar um número maior que 50.
numeros = [1,5,98,5,42,4,5,3,45,78,-1,-8,8]

for numero in numeros:
    if numero >50:
        print("Primeiro número maior que 50, é: ",numero)
        break
print("Números da lista: ",numeros)

print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 