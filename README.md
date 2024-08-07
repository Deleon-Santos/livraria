
# Documentação do Sistema de Cadastro de Livros

## Sumário
1. [Introdução](#introdução)
2. [Requisitos do Sistema](#requisitos-do-sistema)
3. [Estrutura do Código](#estrutura-do-código)
4. [Descrição das Funções](#descrição-das-funções)
5. [Fluxo de Execução](#fluxo-de-execução)
6. [Exemplo de Uso](#exemplo-de-uso)
7. [Conclusão](#conclusão)

## Introdução
O sistema foi desenvolvido para armazenar informações de livros utilizando filtros de entradas e um banco de dados integrado ao código. Este documento visa fornecer uma visão geral do sistema, incluindo a estrutura do código, a descrição das funções e um exemplo de uso.

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)
![SQLite Logo](https://www.sqlite.org/images/sqlite370_banner.gif)

## Requisitos do Sistema
- Python 3.x
- Biblioteca SQLite3

## Estrutura do Código

```python
import sqlite3 as bd

lista=[]

def conectar():
    conex= bd.connect("livraria")#conectar com um banco de dados com o nome "livraria"
    curs= conex.cursor()#o cursor recebe a conexao para manipular o bd
    return curs,conex

def gravar():
    cursor, conexao = conectar()
    cursor.execute("""
        create table if not exists livro(
            id_livro integer primary key autoincrement, 
            nome_livro text, 
            preco_livro real, 
            ano_livro text
        )
    """)
    cursor.execute("insert into livro (nome_livro, preco_livro, ano_livro) VALUES(?,?,?)", (lista[0], lista[1], lista[2]))
    conexao.commit()
    mostrar(cursor, conexao)  # chama a função visualizar cadastro

def mostrar(cursor, conexao):
    cursor, conexao = conectar()
    cursor.execute("select * from livro")
    
    print("ID               Livro                              Preço                  Ano")
    for row in cursor.fetchall():
        linha = row
        if linha:  # formatação para imprimir o resultado como uma tabela
            print(f'{linha[0]:<8}   {linha[1]:<40} {linha[2]:<20.2f} {linha[3]:>5}')
    # fecha o banco após encerrar a consulta
    cursor.close()
    conexao.close()  

# Início da Aplicação
print('******************************LIVRARIA****************************************')
while True:
    while True:
        nome = input("Qual livro deseja adicionar? ")
        if nome:
            nome = nome.title()
            lista.insert(0, nome)
            break
        else:
            print("Informe o nome")
            continue
    
    while True:
        try:
            preco = float(input("Informe o preço do Livro: "))
            if preco:
                lista.insert(1, preco)
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

    finalize = input("\n'S'-sair ou 'C'-continuar: ")
    finalize = finalize.upper()[0]
    
    if finalize in "SC":
        if finalize == "S":
            break
        else:
            continue
    else:
        continue
```

## Descrição das Funções

### `conectar()`
Estabelece a conexão com o banco de dados SQLite chamado "livraria" e retorna o cursor para manipulação do banco de dados e a conexão.

### `gravar()`
Cria a tabela `livro` se não existir, insere um novo registro na tabela com os dados do livro presentes na lista `lista`, e chama a função `mostrar()` para exibir os registros.

### `mostrar()`
Consulta todos os registros da tabela `livro` e os imprime em formato de tabela. Fecha a conexão após a consulta.

## Fluxo de Execução
1. O programa exibe uma mensagem de boas-vindas.
2. Solicita ao usuário o nome do livro, o preço e o ano de lançamento.
3. Valida as entradas.
4. Insere os dados no banco de dados e os exibe.
5. Pergunta ao usuário se deseja continuar ou sair.

## Exemplo de Uso
```python
# Saída esperada ao adicionar um livro:

******************************LIVRARIA****************************************
Qual livro deseja adicionar? Python Programming
Informe o preço do Livro: 49.99
Informe o ano de lançamento do Livro: 2021
ID               Livro                              Preço                  Ano
1        Python Programming                          49.99                2021

'S'-sair ou 'C'-continuar: 
```

## Conclusão
Este sistema simples permite o armazenamento e visualização de informações sobre livros utilizando o SQLite. É possível expandir as funcionalidades para incluir atualização e exclusão de registros, assim como aprimorar a interface de usuário.
