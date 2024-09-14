#Tuplas = São listas de itens que não podem ser alteradas
#São definidas por () e os itens separados por virgulas

#Util para quando queremos garantias que os dados permaneceram os mesmos
#Os itens sempre iniciam com zero
print("---------------------------OS ITENS SEMPRE INICIAM EM 0---------------------------")
frutas = ('Maça','Banan','Laranja')
print(frutas[0])

print("-----------------------------ENCONTRAR ITEM NA LISTA------------------------------")
#Print para separação dos resultados apresentados no terminal 
animais = ('Cachorro','Gato','Coelho')

if 'Gato' in animais:
    print("Gato esta na lista!")
else:
    print("Gato não esta na lista!")