# contar quantas vezes aparec uma palavra em um texto
import os
import time


# os.system('cls')

# texto= "A rapida raposa marrom pulou sobre o cachorro marrom"
# lista=texto.split()
# print (lista)

# texto_final={}
# for palavra in lista:
#     if palavra in texto_final:
#         texto_final[palavra] += 1
#     else:
#         texto_final[palavra]= 1
# print(texto_final)
  

#Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# formula= Xnorm= X -Xmin/Xmax-Xmin

# lista=[10,20,20,40,50]
# menor=min(lista)
# maior=max(lista)
# lista_nova=[]

# for i in lista:
#     lista_nova.append((i - menor)/(maior-menor))
# print(lista_nova)

# Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

#Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm 
# um campo específico faltando.

# os.system('cls')

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# for pessoa in usuarios:
#     if  pessoa["nome"] == "" or pessoa["email"] == "":
#         pessoa["Ativo"]="Falta um campo"
#     else:
#         pessoa["Ativo"]="Tudo ok"

# print(usuarios)


#Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# os.system('cls')
# total= []
# i=0

# for item in vendas:
#     categoria=item["categoria"]
#     valor=item["valor"]
#     if categoria  in total:
        
       
#     else:
#         total.append(categoria)
#         total.append(valor)
#     i += 1 
# print(total)

##################################################################
#  while
# 
# loop para verificar nome.

# os.system('cls')
# while True:
#     try:
#         nome=input("Entre com o seu nome:")
#         if nome.isdigit() or nome.isspace():
#                 print("Não digitar números ou espaços. Digite o seu nome")
#                 time.sleep(3)
#         else:
#              break
#     except ValueError:
#         print("Digitar o seu nome")

# print(f" Seu nome é: {nome}")

# loop para verificar salario.

os.system('cls')
while True:
    try:
        salario=input("Entre com o seu salario:")
        salariook=float(salario.replace(",","."))
        break
    except ValueError:
        print("Digitar um número")

print(f" Seu salario é: {salariook}")
