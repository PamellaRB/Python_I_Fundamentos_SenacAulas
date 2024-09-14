#Dicionario = Armazena dados em pares [chaves - valor]
#Utilizamos chaves {} e cada parte de chave-valor é separado por dois pontos

#Exemplo:
aluno = {
    'Nome':'João',
    'Idade':31
}

#Crie um dicionario chamado pesosas, com as informações de nome, idade e cidade. Em sequência apresente apenas o nome
print("--------------------DEMONSTRANDO APENAS UM RESULTADO DO DICIONARIO--------------------")
pessoas = {
    'Nome':'Pamella Barros',
    'Idade':25,
    'Cidade':'SBC'
    } 

print(pessoas['Nome'])   
#A busca é realizada por chaves

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
print("---------------------------------ATRIBUIÇÃO E INCLUSÃO--------------------------------")
pessoas['Profissão'] = 'Engenheiro'
#Mesmo que não tenhamos criado a chave Profissão, a partir do momento que solicitamos ao código para incluir a informação
#no dicionário, automaticamente ele irá criar a chave e incluir o valor informado. 
print(pessoas)

print("--------------------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#Quero saber se existe a chave Idade na variavel Pessoas
if 'idade' in pessoas:
    print(pessoas['idade'])
else:
    print("A chave informada não foi encontrada")