#JSON é uma estrutura de dados, utilizada para transmitir informações entre servidor e cliente.
#Ele usa pares "chave-valor" (parecido com o dicionario)

{
    "Nome":"João",
    "Idade":14,
    "Habilidades":["Pyhton","Photoshop"],
    "Ativo": True
}

#Valide no site https://jsonlint.com/ se o Jason é valido
#True em python é obrigatório ser em maiusculo
#Porém, em Jason ele reconhece apenas em minusculo
#Sendo assim, caso valide o jason no site informado, altere para "t" minusculo
#Este documento foi criado como Python devido o JSON não permitir comentarios

import json

with open('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\\Aula6\\4.Utilizando_JSON\\dadosjson.json', 
    'r', encoding='utf-8') as arquivo: 
    dados = json.load(arquivo)
    print(dados)
    print(dados["Nome"])