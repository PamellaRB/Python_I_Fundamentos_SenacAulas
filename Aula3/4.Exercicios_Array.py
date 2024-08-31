# 1  - Crie uma lista com cinco nomes de frutas. Em seguida, peça para eles realizarem as seguintes operações:
# a. Acessar e imprimir a segunda fruta da lista.
# b. Substituir a última fruta por outra de sua escolha.
# c. Adicionar uma nova fruta ao final da lista.
# d. Remover a primeira fruta da lista.

#1
frutas = ["Morango","Kiwi","Mamão","Abacate","Uva"]
print(frutas)
#A
print("A segunda fruta é: ",frutas[1])
#B
#Sempre começa em 0, sendo assim, a quinta fruta tem numeração 4
frutas[4] = "Manga"
print(frutas)
#C
frutas.append ("Manga")
#Quando for utilziar o append não é necessario utilizar o sinal de =, utliza os () direto
#.append é responsável por adicionar algo ao Array
#D
#frutas.pop()
#.pop é responsavel por remover o último item da lista, não é necessario incluir valor dentro dos ().
#porém, caso queira escolher onde ele irá excluir, inseir o numero no qual deseja excluir frutas.pop(6)
frutas.pop(0) #Removendo o item 1 da lista
print(frutas)

# 2 - Crie uma lista com cinco nomes de pessoas. Em seguida, realize as seguintes operações:
# a. Adicione dois novos nomes ao final da lista.
# b. Substitua o segundo nome da lista por "Anônimo".
# c. Remova o primeiro nome da lista.
# d. Remova o último nome da lista.

#2
nomes = ["Lucas", "Amanda", "Rafael", "Bianca", "Felipe"]
print(nomes)
#A
nomes.append ("Gabriel")
nomes.append ("Mariana")
print(nomes)
#B
nome2 = nomes[1] = ("Anônimo")
print(nomes)
#C
nomes.pop(2)
#D
nomes.pop()
print(nomes)

# 3 - Crie uma lista com cinco itens que você compraria no supermercado. Em seguida, realize as seguintes operações:
# a. Adicione dois novos itens ao final da lista.
# b. Remova o primeiro item da lista.
# c. Remova o último item da lista.
# d. Adicione um novo item ao final da lista e remova o item "Leite" da lista.

#3
mercado = ["Arroz", "Feijão", "Açúcar", "Café", "Óleo"]
print(mercado)
#A
mercado.append ("Leite")
mercado.append ("Macarrão")
print(mercado)
#B
mercado.remove("Café")
print(mercado)
#C
mercado.pop()
#D
mercado.append ("Pão")
mercado.remove ("Leite")
print(mercado)

# 4 - Crie uma lista com cinco números inteiros. Em seguida, realize as seguintes operações:
# a. Adicione um novo número ao final da lista.
# b. Remova o menor número da lista.
# c. Remova o último número da lista.
# d. Adicione um novo número ao final da lista e remova o primeiro número da lista.

#4
numeros = [1,2,3,4,5]
print(numeros)
#A
numeros.append (6)
print(numeros)
#B
numeros.remove(2)
print(numeros)
#C
numeros.pop()
#D
numeros.append(7)
numeros.pop(0)
print(numeros)
