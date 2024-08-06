import sqlite3 as bd
from datetime import date
lista=[]
#conectar com um banco de dados com o nome "livraria"
conexao= bd.connect("livraria")
#o cursor recebe a conexao para manipular o bd
cursor= conexao.cursor()

cursor.execute("""create table if not exists livros
               (
               id_livro integer primary key, 
               nome_livro text, 
               preco_livro real, 
               ano_livro text
               )
               """)
while True:
    while True:
        nome=input("Qual livro deseja adicionar? ")
        if nome:
            nome=nome.title()
            lista.insert(0,nome)
            break
        else:
            print("Informe o nome")
            continue
    while True:
        preco=float(input("Informe o preço do Livro: "))
        if preco:
            lista.insert(1,preco)
            break        
        else:
            print("Informe o preço")
            continue
    while True:
        ano=input("Informe o ano de lançamento do Livro: ") 
        if ano:
            lista.insert(2,ano) 
            break    
        else:
            print("Informe o ano")
            continue
    finalize=input("""'S'-sair ou 'C'-continuar""")
    finalize=finalize.upper()[0]
    if finalize in "SC":
        if finalize== "S":
            break
        else:
            print(lista)
            continue
        


