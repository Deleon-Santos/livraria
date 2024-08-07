import sqlite3 as bd
from datetime import date

lista=[]


def gravar():
    cursor,conexao=conectar()
    cursor.execute("""
            create table if not exists livro(
                id_livro integer primary key autoincrement, 
                nome_livro text, 
                preco_livro real, 
                ano_livro text
            )
    """)
    
    cursor.execute(" insert into livro (nome_livro, preco_livro, ano_livro) VALUES(?,?,?)" ,(lista[0], lista[1], lista[2]))
    
    conexao.commit()
    cursor.execute(" select * from livro")
    print("ID               Livro                       Preço        Ano")
    for row in cursor.fetchall():
        linha =row
        if linha:
            
            print(f'{linha[0]}   {linha[1]} {linha[2]} {linha[3]}')
            
        
    print("gravados")
    cursor.close()
    conexao.close()



def conectar():

    #conectar com um banco de dados com o nome "livraria"
    conex= bd.connect("livraria")
    #o cursor recebe a conexao para manipular o bd
    curs= conex.cursor()
    return curs,conex

    
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
        print()
        if ano:
            lista.insert(2,ano)
            gravar() 
            break   

        else:
            print("Informe o ano")
            continue
    finalize=input("""\n'S'-sair ou 'C'-continuar""")
    finalize=finalize.upper()[0]
    if finalize in "SC":
        if finalize== "S":
            break
        else:
            print(lista)
            continue
        


