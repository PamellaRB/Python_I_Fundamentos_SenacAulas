#1 - Crie uma lista com seis números inteiros. Em seguida, use um laço for para contar quantos números 
#pares existem na lista e imprimir o resultado.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
numeros = [1,3,12,7,10,5]
contador = 0

for numero in numeros:
        #Se o resto da divisão por 2
        # == Comparação
    if numero % 2 == 0:
                #Se o resto da divisão por 2 for igual (==) de 0
        contador += 1 # variavel contador = contador + 1

print("Existem", contador, "números pares na lista")

#2 - Crie uma lista com seis números inteiros. Em seguida, use um laço for para somar 
#todos os números da lista que são maiores que 5 e imprimir o resultado.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
numeros_inteiros = [4,5,9,12,7,3]
soma = 0

for numeros_inteiros in numeros:
    if numeros_inteiros >5:
        soma += numeros_inteiros 
        #Soma = Variavel Soma + Variavel numeros inteiros que se refere a lista de numeros

print("A soma dos números maiores que 5 é: ",soma)

#3 - Crie uma lista com seis números inteiros. Em seguida, use um laço for para contar 
#quantos números ímpares existem na lista e imprimir o resultado.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
numeros_inteiros2 = [1,7,12,9,78,3]
contador2 = 0

for numeros_inteiros2 in numeros:
    #Variavel de lista    #Nome variavel do for
        #Se o resto da divisão por 2
        # == Comparação
    if numeros_inteiros2 % 2 != 0:
                #Se o resto da divisão por 2 for diferente (!=) de 0
        contador2 += 1 # variavel contador = contador + 1

print("Existem", contador2, "números ímpares na lista")