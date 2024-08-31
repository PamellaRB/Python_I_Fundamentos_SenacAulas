#FOR = Para
#For é responsável por percorrer listas

compras = ["Arroz", "Feijão", "Açúcar", "Café", "Óleo"]

#Os itens que foram inclusos em compras, foram demonstrados em forma de listagem ao utilizar o "For"
#for produto (aqui você nomeia a variavel, o nome da lista por exemplo) in (onde) compras (colocar a variavel onde criou a lista)
for produto in compras:
    print(produto)


#Você possui uma listagem de números, porém, você deseja que todos os numeros listados, sejam multiplicados por 2
#Primeiramente você cria a listagem dos numeors
#Segundo você cria uma variavel vazia para poder ser adicionado os novos numeors
numeros = [1,2,3,4,5,6]
novos_numeros = []

#No for, você cria a variavel de execução e em sequencia referencia a variavel que criou a listagem
for calculo in numeros:
    novos_numeros.append(calculo * 2) 
    #Aqui você adiciona (append) numeros na variavel vazia e entre () realiza o calculo
    #Para realizar o calculo, é necessário que utilize a variavel que criou no for, exemplo, "calculo"
    #pois a variavel "calculo" irá pegar os numeros na lista "numeros" para realizar o calculo
print("Primeiros números: ", numeros)
print("Números da lista multiplicados por 2: ", novos_numeros)


#Na demonstração abaixo iremos validar quais dos numeros dentro da listagem é maior que 10

numeros = [4,6,80,60,5,20,10,8,4,1,7]
contador = 0

for contagem in numeros:
    if contagem >10:
        contador += 1 #(+=) significa que ele ira guardar a variavel, sempre contar

print("Existem ", contador,"números maiores que 10")