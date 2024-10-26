import requests

url = "https://api.github.com/users/PamellaRB"

#API - Quando falamos de API falamos sobre verbos de informação
#GET = Busca de informações
#POST = Envio de informações
#Informação: Os navegadores fazer GET na url, qualquer site que vc navegue as url's realizam
#GET para capitar as informações

#Vamos simular um navegador e utilizar o python para buscar informações:

resposta = requests.get(url)
#aqui estamos buscando a resposta da url que inserimos anteriormente

if resposta.status_code == 200:
    dados_usuario = resposta.json()
    print(dados_usuario)
    print("Nome: ", dados_usuario, ["name"])
    print("Usuário: ", dados_usuario, ["login"])
    print("Seguidores: ", dados_usuario, ["followers"])
    print("Seguindo: ", dados_usuario, ["following"])

#Exercicio 1
print("---------------------------------------------------------------------")
cep = input ("Digite o CEP (Apenas núneros): ")
url = f'https://viacep.com.br/ws/{cep}/json/'
resposta = requests.get(url)

if resposta.status_code == 200:
    endereco = resposta.json()
    print("Endereço: ", endereco ["logradouro"])
    print("Bairro: ", endereco ["bairro"])
    print("Cidade", endereco ["localidade"])
    print("Estado: ", endereco ["estado"])

else:
    print("Falha ao consultar CEP")
