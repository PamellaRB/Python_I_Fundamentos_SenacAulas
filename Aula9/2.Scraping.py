#Web Scraping é o processo de extrair dados de website de forma automatica
#Util para coletar informações de sites que não fornecem API

import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
resposta = requests.get(url)
print(resposta.text) #Irá mostrar o conteudo HTML do site

#Criando um objetio BeautifulSoup
soup = BeautifulSoup(resposta.text, 'html.parser')

#Exibindo o titulo da pagina
print(soup.title.text)

#Extraindo paragrafos da pagina
paragrafos = soup.find_all('p')
for p in paragrafos:
    print(p.text)

print('---------')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

#Usando seltores CSS para informações mais precisas

produtos = soup.find_all('article', class_='product_pod')
print(produtos)

for produto in produtos:
    titulo = produto.h3.a['title']
    preco = produto.find('p', class_='price_color').text
    print(titulo,preco)