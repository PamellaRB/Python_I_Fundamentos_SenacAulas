import requests


print("--------------------------EXERCICIO 1---------------------------")
cep = input ("Digite o CEP (Apenas núneros): ")
url = f'https://viacep.com.br/ws/{cep}/json/'
resposta = requests.get(url)

if resposta.status_code == 200:
    endereco = resposta.json()
    print("CEP: ", endereco ["cep"])
    print("Endereço: ", endereco ["logradouro"])
    print("Complemento", endereco ["complemento"])
    print("Bairro: ", endereco ["bairro"])
    print("Cidade: ", endereco ["localidade"])
    print("UF: ", endereco ["uf"])
    print("Estado: ", endereco ["estado"])
    print("Região: ", endereco ["regiao"])
    print("IBGE: ", endereco ["ibge"])
    print("GIA: ", endereco ["gia"])
    print("DDD: ", endereco ["ddd"])
    print("SIAFI: ", endereco ["siafi"])
else:
    print("Falha ao consultar CEP")


print("--------------------------EXERCICIO 2---------------------------")
import requests

# Exercício 2: Consulta a população estimada de um município pelo código IBGE
print("--------------------------EXERCICIO 2---------------------------")
codigo_ibge = input("Digite o código IBGE do município (por exemplo, 3550308 para SP): ")
url = f'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[{codigo_ibge}]'
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    populacao_estimada = dados[0]['resultados'][0]['series'][0]['serie']['2021']
    print("População estimada:", populacao_estimada)
else:
    print("Falha ao consultar a população do município")

# Exercício 3: Listar municípios de um estado pela sigla
print("--------------------------EXERCICIO 3---------------------------")
sigla_estado = input("Digite a sigla do estado (por exemplo, SP): ")
url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_estado}/municipios'
resposta = requests.get(url)

if resposta.status_code == 200:
    municipios = resposta.json()
    print("Municípios do estado", sigla_estado + ":")
    for municipio in municipios:
        print(municipio['nome'])
else:
    print("Falha ao consultar os municípios do estado")

# Exercício 4: Listar feriados nacionais de um ano
print("--------------------------EXERCICIO 4---------------------------")
ano = input("Digite o ano para consultar feriados nacionais: ")
url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
resposta = requests.get(url)

if resposta.status_code == 200:
    feriados = resposta.json()
    print("Feriados nacionais em", ano + ":")
    for feriado in feriados:
        print(f"{feriado['date']}: {feriado['name']}")
else:
    print("Falha ao consultar os feriados nacionais")

# Exercício 5: Listar estados brasileiros com códigos IBGE
print("--------------------------EXERCICIO 5---------------------------")
url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
resposta = requests.get(url)

if resposta.status_code == 200:
    estados = resposta.json()
    print("Estados brasileiros com códigos IBGE:")
    for estado in estados:
        print(f"{estado['nome']} - Código IBGE: {estado['id']}")
else:
    print("Falha ao consultar os estados brasileiros")

# Exercício 6: Consulta de informações de uma empresa pelo CNPJ
print("--------------------------EXERCICIO 6---------------------------")
cnpj = input("Digite o CNPJ (apenas números) (Senac: 03.709.814/0001-98): ")
url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
resposta = requests.get(url)

if resposta.status_code == 200:
    empresa = resposta.json()
    print("Informações da empresa:")
    print("Nome:", empresa.get("nome"))
    print("Fantasia:", empresa.get("fantasia"))
    print("Atividade principal:", empresa.get("atividade_principal")[0].get("text"))
    print("Logradouro:", empresa.get("logradouro"))
    print("Bairro:", empresa.get("bairro"))
    print("Município:", empresa.get("municipio"))
    print("UF:", empresa.get("uf"))
    print("CEP:", empresa.get("cep"))
else:
    print("Falha ao consultar o CNPJ")

# Exercício 7: Listar cidades que utilizam um código DDD específico
print("--------------------------EXERCICIO 7---------------------------")
ddd = input("Digite o código DDD: ")
url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'
resposta = requests.get(url)

if resposta.status_code == 200:
    ddd_info = resposta.json()
    print(f"Cidades que utilizam o DDD {ddd}:")
    for cidade in ddd_info['cities']:
        print(cidade)
else:
    print("Falha ao consultar o DDD")
