#Array [] é uma coleção ordenada de elementos
#pode ser qualquer tipo (números, strings e listas)
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
frutas = ["maça", "banana", "laranja"]
#Lista de strings
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
numeros = [1,2,3,4,5]
#Lista de Inteiros
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
misturado = ["texto", 21,45.5, True]
#Lista com diferentes tipos de dos

#Array os itens sempre iniciam em zero.
    # 0     1       2

#frutas = ["maça", "banana", "laranja"]
#Posição zero do Array
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
primeira_fruta = frutas [0] #Maça
segunda_fruta = frutas [1] #Banana

print(primeira_fruta)
print(segunda_fruta)
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Modificando um elemento da lista
primeira_fruta = frutas[0] = "uva"
print(primeira_fruta)
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Adicionando elementos
#Adicionar elementos = append
frutas.append("abacaxi")
print(frutas)
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Removendo elementos
frutas.remove("banana") #Removendo banana da lista
frutas.pop() #Remove o ultimo item da lista
print(frutas)
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Manipulando uma lista de numeros
numeros = [10,20,30,40,50]

print("Primeiro número: ", numeros[0])
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Modificando elemento
numeros[2] = 35

#Adicionando elemento
numeros.append(60)
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Removendo um elemento
numeros.remove(35) #Procura e remove o item informado.
print(numeros)