import json

with open ('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\Aula7\\1.lista.json','r') as arquivo:
    lista = json.load(arquivo)
    print(lista)