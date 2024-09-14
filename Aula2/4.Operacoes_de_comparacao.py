#OPERAÇÕES DE COMPARAÇÃO;
#SEMPRE TEREMOS UM RETORNO SE NOSSA PERGUNTA É VERDADEIRA (TRUE) OU FALSA (FALSE)

#IGUALDADE - "=="
#DIFERENTE - "!="
#MAIOR QUE - ">"
#MENOR QUE - "<"
#MAIOR OU IGUAL ">="
#MENOR OU IGUAL "<="

#IGUALDADE
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
preco_produto_a = 50
preco_produto_b = 50

#Gostaria de saber se os preços dos produtos são iguais

#If = Se
if preco_produto_a == preco_produto_b:
#Se o preço A é igual ao preço B
#: representa se minha pergunta for verdadeira
    print("Os produtos são iguais")
    #este espaçamento (tab) informa que esta dentro do if, isso é um bloco de código. Caso não utiliza o espaçamento, significa que o "print"
    #não faz parte do "if"
    #if sempre aguarda uma condição (if condição:)

#DIFERENÇA
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
saldo_cliente_1 = 1200
saldo_cliente_2 = 1500

if saldo_cliente_1 != saldo_cliente_2:
    print("Os valores são diferentes")

#MAIOR QUE
print("---------------------------------------------------------------------------")
#Print para separação dos resultados apresentados no terminal 
faturamento_loja_a = 70000
faturamento_loja_b = 68000

if faturamento_loja_a > faturamento_loja_b:
    print("O faturamento da loja A é maior do que a loja B")
