##1-Solicite ao usuário que insira dois números inteiros. Subtraia o segundo número do primeiro e exiba o resultado.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
num1 = int (input ("Insira o 1º número para subtração: "))
#Se não colocar o int antes do imput o Python irá entender que é apenas para juntar os números, exemplo: 
#Na subtração se colocar o primeiro número como "1" e o segundo como "1", ao invés do resultado da subtração dar "0"
#Irá juntar os dois numero e ficar "11"
#Se utiliza o "input" para poder salvar a informação transmitida pelo usuário. 
num2 = int (input ("Insira o 2º número para subtração: "))

sub = num1 - num2
#Esta variável é o calculo da subtração, é possivel fazer a subtração sem criar variavel, porém, com essa criação fica mais limpo o código
#Sem essa variavel o print seria {print(num1, "-", num2, "=", num1-num2)}

print(num1, "-" ,num2, "=", sub)
#Print é para poder mostrar na tela o que esta escrito entre parenteses "()"
#Não esquecer de colocar virgula entre as informações quando utilizar variavel, caso não coloque, irá dar erro. 

#2 - Peça ao usuário que insira o valor total de uma compra e o valor pago. Calcule e exiba o troco a ser devolvido.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
#UTILIZANDO VALORES INTEIROS
comp = int (input ("Insira o valor total da compra: "))
#Variavel float permite a utilização de números com virgula. 
pag = int (input ("Insira o valor pago: "))
cal = comp - pag
print("Valor compra: ", comp)
print("Valor pago: ", pag)
print("Valor troco: ", cal)

#UTILIZANDO VALORES COM VIRGULA
compra = float (input ("Insira o valor total da compra: "))
#Variavel float permite a utilização de números com virgula. 
pago = float (input ("Insira o valor pago: "))
calc = compra - pago
print("Valor compra: ", compra)
print("Valor pago: ", pago)
print("Valor troco: ", calc)

#3 - Solicite ao usuário que insira três números inteiros. Calcule a soma dos três números e exiba o resultado.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
num1 = int (input("Insira o primeiro número para soma: "))
num2 = int (input("Insira o segundo número para soma: "))
num3 = int (input("Insira o terceiro número para soma: "))

soma = num1 + num2 + num3

print("A soma dos três números inseridos é: ", soma)

#4 - Peça ao usuário que insira as idades de duas pessoas. Calcule e exiba a diferença entre as idades.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
print("Vamos calcular a diferença de idade? ")
idade1 = int (input ("Insira a idade maior: "))
idade2 = int (input ("Insira a segunda idade: "))

dif = idade1 - idade2

print("A diferença entre as idades é ", dif)
