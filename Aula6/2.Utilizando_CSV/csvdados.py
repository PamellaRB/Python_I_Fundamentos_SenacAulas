#CSV são valores separados por virgula

#CSV, ou "Comma-Separated Values" (Valores Separados por Vírgulas), é um formato simples e amplamente utilizado 
# para armazenar dados tabulares. Em um arquivo CSV, cada linha representa um registro, e os valores dos campos 
# dentro de um registro são separados por vírgulas.

#Exemplo:
#nome,idade,email
#João,28,joao@email.com

#Os dados precisam estar dentro do CSV, conforme documento "dados.csv"

#Importar o documento
import csv 
#Como você realizou o import do CSV, não colocar o nome do csv deste arquivo apenas como "csv", caso coloque, 
#o código irá bugar

#No open deve colocar o primeiro parâmetro em sequência caminho do arquivo. 
#Mode = r (r = ler "read")
#newline = quebra de linha

# Abre o arquivo 'dados.csv' no modo de leitura ('r') e o associa à variável 'csvarquivo'
# O bloco `with` garante que o arquivo será fechado automaticamente após o uso.
#precisa incluir o caminho completo
#quando for colocar o caminho, precisa colocas \\, pois, caso deixe apenas uma \, o código irá pensar que você esta
#querendo pular linha
with open('T:\\Cursos Livres\\9900306841_PYTHON_I_FUNDAMENTOS_T09112024\\Pamella Barros\\Aula6\\2.Utilizando_CSV\\dados.csv', 
  mode='r', newline='',encoding='utf-8') as csvarquivo:

  # Usa a função csv.reader para ler o conteúdo do arquivo CSV. 'leitor' será um iterador
    # que retorna cada linha do arquivo como uma lista de valores separados por vírgulas.
    leitor = csv.reader(csvarquivo)

 # Loop que percorre cada linha do arquivo CSV
    for linha in leitor:
        
        # Aqui 'linha' é uma lista de valores que representa uma linha do CSV.
        # Imprime a linha no console.
        print(linha)
