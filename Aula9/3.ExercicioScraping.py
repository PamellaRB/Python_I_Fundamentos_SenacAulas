import requests
from bs4 import BeautifulSoup

# URL da página de citações
url = 'http://quotes.toscrape.com/'
resposta = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    # Cria o objeto BeautifulSoup
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Exibindo o título da página
    print("Título da página:", soup.title.text)
    
    # Extraindo todas as tags <span> e exibindo seu conteúdo
    spans = soup.find_all('span')
    print("\nConteúdo das tags <span>:")
    for span in spans:
        print(span.text)
    
    # Extraindo e exibindo os nomes dos autores de cada citação
    autores = soup.find_all('small', class_='author')
    print("\nAutores das citações:")
    for autor in autores:
        print(autor.text)
else:
    print("Erro ao acessar a página:", resposta.status_code)
