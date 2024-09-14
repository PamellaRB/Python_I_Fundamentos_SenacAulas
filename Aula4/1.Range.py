#Range = Função para gerar uma sequência de números 
# for i in range(5):

#Tipos de Range:
#range(5) = range (fim)
#range(0,20) = range (inicio, fim)
#range (0,11,2)= range (inicio, fim, passo)

#range(5) = range (fim)
print("--------------DEMONSTRAÇÃO EM FIM---------------------------")
for i in range(5):
#Será executado do numero 0 ao 4, criando:
#[0,1,2,3,4]
#O Range serve para fornecer uma sequencia de números sem a previa digitação dele, conforme demonstrado no Array
    print(i)
    #Como esta utilizando o for, o print precisa estar dentro da sua execução para poder gerar seu resultado
    #i é o nome da variavel, você pode nomear de acordo com sua preferencia. 

print("------------------------------------------------------------")
#Print para separação dos resultados, para não confundir na aparição no terminal.

#range(0,20) = range (inicio, fim)
print("--------------DEMONSTRAÇÃO EM INICIO E FIM------------------")
for i in range(2,7):
#Será executado do numero 2 ao 6, criando:
#[2,3,4,5,6]
#Conforme demonstrado anteriormente o Array sempre se inicia em 0, por este motivo a aparição do resultado é um numero a menos
#do que o que foi declarado na variavel. 
    print(i)

print("------------------------------------------------------------")
#Print para separação dos resultados, para não confundir na aparição no terminal.

print("-------------DEMONSTRAÇÃO EM INICIO, FIM E PASSO------------")
print("------------------------------------------------------------")
#range (0,11,2)= range (inicio, fim, passo)
#Abaixo será demonstrado dois tipos de range de inicio, fim e passo
#Na primeira será iniciado com 0, sendo assim, a tendencia dos números a serem apresentados será em par
#Na segunda será iniciado com 1, sendo assim, a tendencia dos números a serem apresentados será em ímpar

print("--------------INICIADO COM 0 = DEMONSTRAÇÃO PAR ------------")
for i in range (0,11,2):
#Será executado do numero 0 ao 11, porém, a cada número irá "pular" dois números, criando:
#[0,2,4,6,8,10]
    print(i)

print("------------------------------------------------------------")
#Print para separação dos resultados, para não confundir na aparição no terminal.

print("------------INICIADO COM 1 = DEMONSTRAÇÃO ÍMPAR ------------")
#range (0,11,2)= range (inicio, fim, passo)
for i in range (1,11,2):
#Será executado do numero 0 ao 11, porém, a cada número irá "pular" dois números, criando:
#[1,3,5,7,9,11]
    print(i)

print("------------------------------------------------------------")
#Print para separação dos resultados, para não confundir na aparição no terminal.
