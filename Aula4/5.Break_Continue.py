#Breek = Serve para poder parar o código quando ele estiver em uma execução de loop
#for/while condição:
    #if condição_para_parar:
        #break
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
for i in range (1,11):
    #Se o i for igual a 5
    if i == 5:
        break #Parar o loop de repetição
print(i)

#Continue = Faz com que o Loop pule e execução do bloco de código e vá diretamente para a proxima interação
# for/while condição:
    #if condição_para_pular:
        #continue
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
for i in range(1,6):
    if i == 3:
        continue
    print(i)

#Exercicio Break
#Vamos criar um código que encontre e imprima o primeiro número divisivel por 7. Se encontrar um, o loop deve parar.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
numeros = [12,18,24,35,42,55]

for numero in numeros:
    if numero % 7 == 0:
    #% significa "O resto". Se os numeros da condição tiver como resto da divisão por 7 igual a 0
        print("O primeito número dividido por 7 é: ", numero)
        break
    print("O número ", numero, "não é divisivel por 7!")

#Exercicio Continue
#Vamos criar um código que percorra uma lista de números e imprima apenas numeros pares, ignorando os impares.
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 

numeros = [1,2,3,4,5,6,7,8]

for numero in numeros:
    #Se o resto da divisão por 2 for diferente de 0 o continue faz o processo ir para o proximo número.
    if numero % 2 != 0:
        continue
    
    print("Numero par: ", numero)