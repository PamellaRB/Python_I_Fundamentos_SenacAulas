
import csv 

### Exercício 1: Criação do Arquivo CSV de Produtos
#Crie um arquivo chamado `produtos.csv` que contenha informações sobre cinco produtos. 
# Cada linha deve ter as seguintes colunas: 
#ID, Nome, Preço e Categoria.

#Realizado no arquivo produtos.csv

### Exercício 2: Leitura do Arquivo CSV
#Escreva um código em Python que leia o arquivo `produtos.csv` 
# que você criou e armazene os dados em uma lista de dicionários.

dicionario = []

with open('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\\Aula6\\3.ExercicioCSV\produtos.csv', 
  mode='r', newline='',encoding='utf-8') as csvarquivo: 
    leitor = csv.DictReader(csvarquivo)
  #se utilizar o "csv.DictReader o código consegue destinguir linhas de colunas"
    for linha in leitor: 
        dicionario.append(linha)
    print(linha)

print(dicionario)


print('-------------------------------------------------------------------------------')

### Exercício 3: Exibindo Nomes dos Produtos
#Utilizando um loop `for`, exiba apenas os nomes de todos os produtos contidos no arquivo `produtos.csv`.

for linha in dicionario: 
        print(linha['Nome'])  # Exibe apenas a coluna 'nome'

print('-------------------------------------------------------------------------------')

### Exercício 4: Exibindo Produtos Acima de um Certo Preço
#Escreva um código que, usando um loop `for`, exiba os nomes e preços dos produtos que custam mais de R$ 1000,00.

for linha in dicionario:
        #preco = float(linha['Preço'])  # Converte o preço para float
        if float(dicionario["Preço"]) > 1000:  # Verifica se o preço é maior que 1000
            print(dicionario["Nome"], ': ', dicionario["Preço"])

print('-------------------------------------------------------------------------------')

