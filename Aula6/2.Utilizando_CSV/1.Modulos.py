
#Modulo é um arquivo que contem devinições e instruções.
#Organização (Para dividir o código em parte)
#Reutilização (Usar o mesmo código em diferentes projetos)

import math #Funções matemáticas
import os #Interagir com sistema operacional (Windows)
from datetime import datetime

#Calcular a raiz quadrada de 16 - Utilizando função do próprio Python math
print(math.sqrt(16))
print("-----------------------------------------------------------")
print(os.getcwd()) #Exibe o diretório de trabalho atual.


print("-----------------------------------------------------------")
#Separação de códigos

#Informar a hora atual utilizando o import do datetime
agora = datetime.now()
print("A hora atual é: ", agora)

print("-----------------------------------------------------------")
