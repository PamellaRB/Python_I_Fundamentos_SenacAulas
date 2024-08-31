#Elif = Se não (Utilizado para testar varias condições)

idade = int (input("Informe sua idade: "))

#Iremos criar um código com a condição de idades:
# 12 anos = Criança
# 17 anos = Adolecente
# 18+ = Adulto

if idade <12:
    print ("Você é uma criança.")
elif idade >=12 and idade <18:
    print ("Você é um adolecente")
else:
    print ("Você é um adulto!")