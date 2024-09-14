#1 - Escreva um código para imprimir a tabuada do 5, de 5 até 50, usando a função range().

#Tabuada fazendo de 5x1 até 5x50
print("----------------TABUADA FAZENDO DE 5X1 ATÉ 5X50----------------")
for i in range(5, 51):
    print("5 x", i, "=", 5 * i)

#Para realizar a tabuada basta declarar dentro do range que o número irá iniciar e finalizar com 5, como ele se inicia em 0
#terá que colocar que o numero inicial será 5 e o final 51, para que apareça o número 50 na tabuada
#for i in range(5, 51):
#Para poder realizar a descrição da tabuada, poderá executar dentro do "print"
#print       (                 "5 x"                      ,            i        ,          "=",        5 * i)
# utilizando (""), o que estiver nele será escrito na tela | i = váriavel do for | escrito na tela | calculo da tabuada

print("---------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

print("----------------TABUADA FAZENDO DE 5X1 ATÉ 5X10----------------")
#para utilizar desta forma, basta utilizar o range com o "Pulo", então coloque dentro do range que irá pular de 5 em 5
for i in range(5, 51,5):
    print("5 x", i, "=", 5 * i)

print("---------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#2 - Faça uma contagem regressiva de 10 até 1. Use um laço for e a função range() 
# para contar de 10 até 1 e imprimir cada número.
print("------------------CONTAGEM REGRESSIVA DE 10 < 1----------------")
for i in range(1,10,-1):
    #aqui você coloca que o numero inicial é 1, e que você deseja contar até o 10, e utiliza o "pular", para poder realizar
    #a contagem regressiva, sendo assim, se numeros positivos sempre irá contar para cima >, utilizando numeros negativos
    #irá contar para baixo<
    print(i)

#3 - Escreva todos os números pares de 2 até 20. Use um laço for junto com a função range() 
# para gerar e imprimir esses números.
for i in range (2,21,2):
    #Utilizando o numero 2, por ele ser um número par e sua taboada ser de 2 em 2, todos seus números serão possitivos
    #sendo assim irá aparecer a taboada do dois completa, porém, como o exercicio pede para demonstrar os números pares
    #de 2 até 20, basta colocar o print sem a utilização do texto, conforme primeiro exercicio
    print(i)