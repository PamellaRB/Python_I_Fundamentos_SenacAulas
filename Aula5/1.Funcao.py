#Função = Reutilização de código
#Utilizado para: Organização; Manutenção de código com facilidade; Reutilização

#def nome_da_funcao():
    #código da função
#Def = Palavra chave que define a função
#() = Pode definir um parametro ou não. Um parametro é um valor de entrada
#: = Inicio do bloco de código

def saudacao():
        print("Olá, mundo")

print("-----------------------EXECUÇÃO DA FUNÇÃO-----------------------")
saudacao()
saudacao()
saudacao()
saudacao()
saudacao()


#() = Pode definir um parametro ou não. Um parametro é um valor de entrada
#Parametros são variaveis que passamos para função
#No caso de nome, obriga que seja incluso um nome na função para que ela seja executada
def saudacao2(nome):
    print("Olá ", nome)


print("-----------------------EXECUÇÃO DA FUNÇÃO-----------------------")
saudacao2('Pamella')
saudacao2('Lucas')


#Utilizando mais de um parametro e utilizando return
#No caso da soma, necessario incluir dois valores na função, conforme definido
#Return é para retornar um valor após sua execução
def soma (a,b):
    return a + b

#Sinal de = é atribuição
resultadoSoma = soma(5,3)
print("-----------------------EXECUÇÃO DA FUNÇÃO-----------------------")
print(resultadoSoma)

def quadrado(numero):
    return numero**2

resultado = quadrado(4)
print(resultado)

print(quadrado(9))