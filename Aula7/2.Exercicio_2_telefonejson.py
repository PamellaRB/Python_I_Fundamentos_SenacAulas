import json

with open ('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\\Aula7\\2.Exercicio_2_telefone.json','r', encoding='utf-8') as arquivo:
        contato = json.load(arquivo)
        contato["Biblioteca Cultural São Bento"]
        print(contato)