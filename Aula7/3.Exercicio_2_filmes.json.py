# import json

# with open ('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\\Aula7\\3.Exercicio_2_filmes.json','r', encoding='utf-8') as arquivo:
#         filmes = json.load(arquivo)
#         jsonformatado=json.dumps(filmes,indent=4, ensure_ascii=False)
#         print(jsonformatado)
#         print("---------------------------------------------------------------------------")
#         for filme in filmes:
#                 print(filme['titulo'])
#         print("---------------------------------------------------------------------------")
#         # Exibir os títulos dos filmes dirigidos por Christopher Nolan
#         for filme in filmes:
#                 if filme['diretor'] == 'Christopher Nolan':
#                         print(filme['titulo'])

ListaFilmes = []
contagem_genero = []

for filme in ListaFilmes:
        genero = filme ["gênero"]
        if contagem_genero in genero:
                contagem_genero[genero] =+1
        else:
                contagem_genero[genero] =1

print(contagem_genero)
