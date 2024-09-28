#1 - Crie uma função chamada par_ou_impar que recebe um número como parâmetro e verifica se ele é par ou ímpar. 
# A função deve imprimir "Par" se for par e "Ímpar" se for ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

# Testando a função
print("----------------------------------SAÍDA PAR-------------------------------------------")
par_ou_impar(10)  # Saída: Par
print(par_ou_impar)
print("---------------------------------SAÍDA ÍMPAR------------------------------------------")
par_ou_impar(7)   # Saída: Ímpar
print(par_ou_impar)


print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#2 - Crie uma função chamada `calcular_media` que recebe três notas como parâmetros e retorna a média delas.

def calcular_media(nota1, nota2, nota3):
    return (nota1+nota2+nota3)/3

# Testando a função
resultado = calcular_media(8, 9, 7)
print("-------------------------CALCULO MÉDIA - RESULTADO: 8----------------------------------")
print(resultado)  # Saída: 8.0


print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#3 - Crie uma função chamada contar_letras que recebe uma string como parâmetro e retorna o número de letras dessa string.

def contar_letras(string):
    return len(string)
#O len() é uma função embutida do Python que retorna o número de itens em um objeto, como o comprimento de uma sequência 
# ou o número de elementos em uma lista. No caso de uma string, len() retorna a quantidade de caracteres presentes nela, 
# incluindo espaços e caracteres especiais.


# Testando a função
print("-------------------------CONTAGEM LETRAS - RESULTADO: 6-------------------------------")
quantidade = contar_letras("Python")
print(quantidade)  # Saída: 6


print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#4 - Crie uma função chamada tabuada que recebe um número como parâmetro e imprime a tabuada de 1 a 10 desse número.

def tabuada(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

#A função range() em Python é usada para gerar uma sequência de números
print("--------------------------------RESULTADO TABUADA------------------------------------")
# Testando a função
tabuada(5)

# Saída:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#...
#5 x 10 = 50

#5 - Crie uma função chamada soma_lista que recebe uma lista de números como parâmetro e retorna a soma de todos os 
# elementos dessa lista.

def soma_lista(numeros):
    return sum(numeros)

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#Sum = É usada para somar os itens de uma sequência, como uma lista ou tupla. 
# Ela percorre a sequência e retorna a soma de todos os elementos numéricos.
print("--------------------------------RESULTADO SOMA = 15-----------------------------------")
# Testando a função-
numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(numeros)
print(resultado)  # Saída: 15


print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#6 - Crie uma função chamada maior_numero que recebe uma lista de números como parâmetro e retorna o maior número dessa lista.

def maior_numero(numeros):
    return max(numeros)

#Max =  É usada para retornar o maior valor de uma sequência ou conjunto de valores. 
#Ela percorre todos os itens e retorna o maior deles.

# Testando a função
numeros = [10, 23, 5, 78, 4]
resultado = maior_numero(numeros)
print("--------------------------------RESULTADO MAIOR NUMERO = 78--------------------------")
print(resultado)  # Saída: 78

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#7 - Crie uma função chamada soma_pares que recebe uma lista de números e retorna a soma de todos os 
# números pares presentes na lista.

def soma_pares(numeros):
    soma = 0
#Aqui, a variável soma é inicializada com o valor 0. Ela será usada para acumular a soma de todos 
# os números pares presentes na lista.
    for numero in numeros:
        if numero % 2 == 0:
        #Esta linha verifica se o número atual (numero) é par. A expressão numero % 2 == 0 usa o operador módulo (%), 
        # que retorna o resto da divisão do número por 2. Se o resto for 0, isso significa que o número é divisível 
        # por 2, ou seja, ele é par.
            soma += numero
    return soma

# Testando a função
numeros = [10, 21, 32, 43, 54]
resultado = soma_pares(numeros)
print("-------------------------------------RESULTADO SOMA = 96---------------------------")
print(resultado)  # Saída: 96

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 