import json

with open ('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\\Aula7\\3.Exercicio_1_livros.json','r', encoding='utf-8') as arquivo:
        livros = json.load(arquivo)
        jsonformatado=json.dumps(livros,indent=4, ensure_ascii=False)
        print(jsonformatado)

