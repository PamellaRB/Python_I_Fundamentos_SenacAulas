#1 - Crie um dicionário chamado aluno com as chaves 'nome' e 'curso'. Verifique se a chave 'idade' existe no dicionário. 
# Se existir, mostre o valor correspondente. Caso contrário, exiba uma mensagem dizendo que a chave não foi encontrada.

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
print("------------------------DEMONSTRAÇÃO VALOR DICIONARIO ALUNO---------------------------")

aluno = {
    'Nome':'Pamella',
    'Curso':'Python Fundamentos'
}

print(aluno)

print("---------------------------DEMONSTRAÇÃO VALOR CHAVE IDADE----------------------------")
if 'Idade' in aluno:
    print(aluno['Idade'])
else:
    print("A chave informada não foi encontrada")


#2 - Crie um dicionário chamado pessoa com as chaves 'nome', 'idade' e 'cidade'. 
# Em seguida, remova a chave 'cidade' do dicionário e mostre o dicionário atualizado.

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
print("------------------------DEMONSTRAÇÃO VALOR DICIONARIO ALUNO---------------------------")

pessoa = {
    'Nome':'Pamella',
    'Idade':26,
    'Cidade':'SBC'
}
print(pessoa)

print("---------------------------------EXCLUSÃO CHAVE CIDADE--------------------------------")

pessoa.pop ('Cidade')
#Função pop realiza a exclusão
print(pessoa)

#3 - Crie um dicionário chamado carro com as chaves 'marca', 'modelo' e 'ano'. 
# Em seguida, mostre todas as chaves e valores no formato "chave: valor" utilizando for.
print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
carro = {
    'Marca':'Chevrolet',
    'Modelo':'Celta',
    'Ano':2006
    }
print("------------------------DEMONSTRAÇÃO VALOR DICIONARIO CARRO---------------------------")
print(carro)

print("---------------1º OPÇÃO:DEMONSTRAÇÃO VALOR DICIONARIO CHAVE:VALOR---------------------")

for carros in carro:
    print(carros, ":", carro[carros])
#carros = nome da variavel for
#in = onde irá procurar os itens
#print(variavel, ":", dicionario[variavel])

print("---------------2º OPÇÃO:DEMONSTRAÇÃO VALOR DICIONARIO CHAVE:VALOR---------------------")

for chave, valor in carro.items():
        print(chave, ':', valor)

#chave = nome variavel (chave, valor) - Colocando duas variaveis
#in = onde
#carro.items = dificionario.items()

#4 - Crie um dicionário chamado familia que contenha dois dicionários internos, um para pai (com as chaves 'nome' e 'idade') 
# e outro para mãe (com as mesmas chaves). Em seguida, mostre o nome do pai e a idade da mãe.
print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
familia = {
    'Pai': {
        'Nome': 'Odilon',
        'idade': 59
    },
    'Mãe': {
        'Nome': 'Maria',
        'Idade': 51
    }
}
print("------------------------DEMONSTRAÇÃO VALOR DICIONARIO FAMILIA-------------------------")
print(familia)

print("-----------DEMONSTRAÇÃO VALOR DICIONARIO NOME PAI E IDADE MÃE-------------------------")
print(familia['Pai']['Nome'])
print(familia['Mãe']['Idade'])

#5 - Crie um dicionário chamado `estoque` onde as chaves são nomes de produtos (por exemplo, `'camiseta'` e `'calça'`). 
# Cada produto deve ter uma lista como valor, contendo a quantidade disponível e o preço do produto. 
# Em seguida, mostre a quantidade disponível de um dos produtos.
print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
estoque = {
    'Camiseta': {
        'Quantidade Estoque':30, 
        'Valor':49.99
                },
    #Também pode ser estruturado assim:
    #'Camiseta': [30, 49.99],
    'Calça': {
        'Quantidade Estoque':15, 
        'Valor':79.90
            }
}
print('----------------------------------DICIONARIO ESTOQUE----------------------------------')
print(estoque)

print('------------------------------------QUANTIDADE CALÇA----------------------------------')
print(estoque['Calça']['Quantidade Estoque'])

