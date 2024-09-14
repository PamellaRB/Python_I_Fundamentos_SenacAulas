#OPERAÇÕES LOGICAS

#AND = E (Todas as analises das condições devem ser TRUE, para entrar no IF)
#OR = OU (Se ao menos uma das condições for TRUE, para entrar no IF)
#NOT = Não (Utilizada para trocar o sentido da variavel, ou seja, se a condição for TRUE ela passa a ser FALSE)

#UTILIZANDO O AND
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
temperatura = int (input ("Digite a temperatura: "))
umidade = int (input("Digite a umidade do ar: "))

#Se a temperatura for maior que 25 e a umidade maior que 60. Então o dia esta quente e umido

if temperatura > 25 and umidade > 60:
#Validando se ambas as variaives são verdadeiras (AND)
    print("O dia esta quente e umido")
else: 
    print("O dia esta frio e seco")

#UTILIZANDO O OR
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
hora_atual = int (input("Digite a hora atual sem os minutos (0-23): "))
if hora_atual < 9 or hora_atual > 18:
#Validando se ao menos uma das variaveis for verdadeira (OR)
    print("Horario comercial")
else: 
    print("Fora do Horario comercial")

#UTILIZANDO O NOT
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
chovendo = input ("Esta chovendo? (sim/não)")
#NOT irá converter a resposta do usuário

if not chovendo == "sim":
    print("Você pode sair sem guarda-chuva")
else:
    print("Leve o guarda-chuva")
