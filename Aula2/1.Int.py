# + quando é texto ele junto (Agregação), para utilizar a agragação não converter a variavel em int
# + quando é numero ele soma, para utilizar a soma, converter a variavel em int
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#SOMA:
#Ele recebe o texto do usuario e converte para o tipo int.
num1 = int (input ("Digite o primeiro numero: "))
num2 = int (input ("Digite o segundo numero: "))

soma = num1 +  num2
print ("A soma dos números é: ")
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#AGREGAÇÃO
#Ele recebe o texto do usuario. Não insere "int" antes do input. 
num1 = input ("Digite o primeiro numero: ")
num2 = input ("Digite o segundo numero: ")

soma = num1 +  num2
print ("A agregação dos números é: ")
