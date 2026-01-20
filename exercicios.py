# transacao = {'valor': 12000, 'hora': 20}

# if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
#     print("Transação suspeita")
# else:
#     print("Transação normal")

###################################################################

# for i in range(2,6)
#     print i = 2,3,4,5


#####################################################################
# lista=["rafael","Carlos","Luciano"]
# for pessoa in lista:
#      print(pessoa)

####################################################################
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

###################################################################
# nome = ['Luciano']
# for letra in nome:
#     print(letra)

##################################################################

# list(range(5, 10))
# [5, 6, 7, 8, 9]

# list(range(0, 10, 3))
# [0, 3, 6, 9]

# list(range(-10, -100, -30))
# [-10, -40, -70]

##################################################################
# Contar  a quantidade de palavras em um texto.

# texto= "A rapida raposa marrom pula sobre o cachorro preguica raposa pula"

# texto = "a raposa marrom salta sobre o cachorro raposa preguiçoso raposa"
# palavras = texto.split()
# contagem_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)

#########################################################################
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

#####################################################################

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "livros", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)