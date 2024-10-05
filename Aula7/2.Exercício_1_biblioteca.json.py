import json

with open ('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\Aula7\\2.Exercício_1_biblioteca.json','r', encoding='utf-8') as arquivo:
        lista = json.load(arquivo)
        print("Nome da Biblioteca: ", lista ["Biblioteca"])
        print("Endereço da Biblioteca: ",lista["Endereço"])

# with open ('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\Aula7\\2.biblioteca.json','r', encoding='utf-8') as arquivo:
#     lista = json.load(arquivo)
#     print("Nome da Biblioteca: ", lista[0] ["Biblioteca"])
#     print("Endereço da Biblioteca: ",lista[0]["Endereço"])

#Como no arquivo biblioteca.json foi desenvolvido como lista, para funcionar precisa mencionar qual linha da lista 
#vai ser lida, sendo assim, precisa colocas [0] para indicar a primeira linha, porém, desta forma só irá funcionar sempre
#a primeira linha.
#Como estava no arquivo json:
# [
#     {
#         "Biblioteca":"Central da Cidade",
#         "Endereço":"Av. Paulista, 1000 - São Paulo, SP",
#         "Nº de Livros:":120000,
#         "Horário Funcionamento:":"Segunda a sexta, das 9h às 19h | Sábados, das 10h às 14h"
#     },
#     {
#         "Biblioteca":"Municipal Prof. João Pereira",
#         "Endereço":"Rua das Flores, 250 - Rio de Janeiro, RJ",
#         "Nº de Livros":80000,
#         "Horário Funcionamento":"Segunda a sexta, das 9h às 19h | Sábados, das 10h às 14h"
#     }