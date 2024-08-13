"""Sistema desenvolvido para amazenar informações de livros usando filtros de 
entradas e banco de dados integrado ao codigo"""

import sqlite3 as bd

lista=[]

def conectar():
    conex= bd.connect("livraria")#conectar com um banco de dados com o nome "livraria"
    curs= conex.cursor()#o cursor recebe a conexao para manipular o bd
    return curs,conex

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
    
    mostrar(cursor,conexao)#chama a função visualizar cadastro

def mostrar(cursor,conexao):
    cursor,conexao=conectar()
    cursor.execute(" select * from livro")
    
    print("ID               Livro                              Preço                  Ano")
    for row in cursor.fetchall():
        linha =row
        if linha: #formaataçã para imprimir o resultados como uma tabela
            print(f'{linha[0]:<8}   {linha[1]:<40} {linha[2]:<20.2f} {linha[3]:>5}')
    #fecha o banco apos encerrar a consulta   
    cursor.close()
    conexao.close()  


#Inicio da Aplicação
print('******************************LIVRARIA****************************************')
while True:
    while True:
        nome=input("Qual livro deseja adicionar? ")
        if nome:
            nome=nome.title()#insere maiusculas na primeira letra de nome e sobrenome
            lista.insert(0,nome)
            break
        else:
            print("Informe o nome")
            continue
    
    while True:
        try:
            preco=float(input("Informe o preço do Livro: "))
            if preco:
                lista.insert(1,preco)
                break        
            else:
                print("Informe o preço")
                continue
        except ValueError:
            print('Informe um valor numérico')
    
    while True:
        try:
            ano = int(input("Informe o ano de lançamento do Livro: "))
            ano = str(ano)
            
            if len(ano) == 4:
                lista.insert(2, ano)
                gravar()
                break
            else:
                print("Informe o ano no formato (aaaa)")
        except ValueError:
            print("Informe o ano no formato aaaa")

    finalize=input("""\n'S'-sair ou 'C'-continuar: """)#pode se encerrado precionando "s" para sair
    finalize=finalize.upper()[0]
    
    if finalize in "SC":
        if finalize== "S":
            break
        else:
            continue
    else:
        continue
        
#finaly


