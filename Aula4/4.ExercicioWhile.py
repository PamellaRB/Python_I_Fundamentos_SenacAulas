#1 - Escreva um código que execute uma contagem regressiva de 10 a 1 e, ao final, exiba a mensagem "Olá mundo!".
print("---------------------CONTAGEM DE 10 ATÉ 1 COM WHILE---------------------")
contador = 10
#Defina a variavel contador, como no exercicio pede para que seja feito uma contagem regressiva de 10, deverá ser incluso
#que o contador é igual ao número maior, ou seja, contador = 10
while contador >=0:
    #Equanto a variavel contador não for maior 0
    contador = contador - 1
    #Sera realizado a contagem regressiva, que será o contador que se iniciou em 10, diminuindo sempre 1 número
    print("Contagem ", contador)
    #Até chegar em 0, será realizado a contagem
print("Olá Mundo!")
#Quanto chegar em 0, será exibido a mensagem. 
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#2 - Peça ao usuário para adivinhar um número entre 1 e 20. O loop continuará até que o usuário acerte o número. 
# Informe ao usuário se o palpite foi maior ou menor que o número correto.
#**Dica:** Defina um número secreto e compare os palpites do usuário com esse número.

print("---------USUÁRIO ADIVINHAR UM NÚMERO SECRETO, DECLARADO NA VARIAVEL--------")
numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe um número entre 1 até 20: "))
    if palpite < numero_secreto:
        print("O número inserido é menor que o número secreto!")
    elif palpite >20:
        print("Você inseriu um número maior que o limite!")
    else:
        print("O número inserido é maior que o número secreto!")
print("Você acertou o número secreto")

print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

#3 - Crie um programa que peça ao usuário para inserir notas (valores numéricos). 
# O programa deve continuar pedindo notas até que o usuário insira um valor negativo. 
# Quando isso acontecer, o programa deve calcular e exibir a média das notas inseridas.
# **Dica:** Use um loop `while` para acumular as notas e contar quantas foram inseridas antes de calcular a média.
# Inicializamos as variáveis com 0:

print("---------LOOP DE CALCULO DE MÉDIA DE NOTA ATÉ INSERIR Nº NEGATIVO--------")

nota = 0          # Armazena a nota inserida pelo usuário (inicializada como 0).
contador = 0      # Contador que armazena quantas notas válidas foram inseridas.
soma = 0          # Variável que acumula a soma de todas as notas inseridas.

# O loop vai rodar indefinidamente até que uma condição de saída seja atingida.
# Inicializamos as variáveis
nota = 0          # Armazena a nota inserida pelo usuário.
contador = 0      # Contador que armazena quantas notas válidas foram inseridas.
soma = 0          # Variável que acumula a soma de todas as notas inseridas.

# O loop continua enquanto a nota for maior ou igual a zero
while nota >= 0:
    nota = int(input("Insira sua nota: (insira um número negativo para parar)\n"))

    # Só processa a nota se ela for maior ou igual a 0 (válida).
    if nota >= 0:
        soma += nota
        contador += 1

# Após o loop, verificamos se ao menos uma nota válida foi inserida.
if contador > 0:
    # Se sim, calculamos a média dividindo a soma total pelo número de notas.
    media = soma / contador
    print("A média das notas é: ", media)
else:
    # Se nenhuma nota válida foi inserida (contador é 0), exibimos uma mensagem informando isso.
    print("Nenhuma nota válida foi inserida!")
