#1 - Crie um programa que peça ao usuário para digitar o preço de um produto e a quantidade comprada. 
#Verifique se o preço é maior que 50 reais e se a quantidade é maior que 10. 
#Se ambas as condições forem verdadeiras, exiba "Você recebe um desconto!".
#Caso contrário, exiba "Sem desconto disponível". Inclua o else em sua solução.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
valor_produto = float(input ("Digite o preço do produto: "))
quantidade = int (input("Digite a quantidade de compra: "))

if valor_produto > 50 and quantidade > 10:
    print ("Você recebe desconto")
else:
    print("Sem desconto disponível")

#2- Crie um programa que peça ao usuário para digitar a sua idade e se possui um código de desconto (sim/não). 
# Se a idade for maior que 50 ou se o usuário tiver um código de desconto, exiba a mensagem "Você tem direito ao desconto!". 
# Caso contrário, exiba "Sem desconto disponível". Inclua o else em sua solução.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
idade = int (input("Informe sua idade: "))
desconto = input ("Possui código de desconto? (Sim/Não) ")

#Ao invés de utilizar o "or" é possível urilizar o Upper ou Lower para tratar a informação do usuário
#Upper = Ele converte a string inteira para maiusculo
#Lower = Ele converte a string inteira para minusculo
#Capitalize = Ele converte a primeira linha da string com maíusculo

#A aplicabilidade seria desta forma:
#if idade >50 or desconto.upper () == "sim":
#Sempre irá abrir e fechar parenteses para aplicar a condição

#O motivo de utilizar "or" ao invés de "and" é devido o "and" sempre buscar parametros verdadeiros "true", então, caso sua
#condição não for 100% verdadeira o código poderá quebrar.

if idade > 50 or desconto == "Sim" or "sim":
    print("Você tem direito ao desconto!")
else:
    print("Sem desconto disponível!")

#3 - Crie um programa que peça ao usuário para digitar um nome de usuário. Verifique se o nome digitado não é "Joao". 
# Se a condição for verdadeira, exiba "Acesso permitido, [nome]!". Caso contrário, 
# exiba "Joao não pode ser usado como nome de usuário". Inclua o else em sua solução.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
nome_usuario = input ("Informe seu nome: ")

if nome_usuario == "Joao" or "João":
    print("Acesso permitido, João!")
else:
    print("Joao não pode ser usado como nome de usuário")

# 4 - Crie um programa que peça ao usuário para digitar suas notas em três provas. 
# Verifique se todas as notas são 6 ou mais. Se forem, exiba "Você passou em todas as provas!". 
# Caso contrário, exiba "Você não passou em todas as provas". Inclua o else em sua solução.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
prova1 = float (input("Informe o valor da sua nota na prova 1: "))
prova2 = float (input("Informe o valor da sua nota na prova 2: "))
prova3 = float (input("Informe o valor da sua nota na prova 3: "))

#soma_prova = prova1 + prova2 + prova3

if prova1 and prova2 and prova3 >= 6:
    print("Você passou em todas as provas!")
else: 
    print("Você não passou em todas as provas")

# 5 - Crie um programa que peça ao usuário para digitar seu nome e idade. Verifique se o nome 
# digitado não é "admin" ou se a idade é menor que 18. Se qualquer uma das condições for verdadeira, 
# exiba "Acesso negado". Caso contrário, exiba "Acesso permitido". Inclua o else em sua solução.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
nome = input ("Informe seu nome: ")
idade = int (input("Informe sua idade: "))

if nome != "admin" or idade <18:
    print("Acesso negado")
else:
    print("Acesso permitido")