
# Documentação do Sistema de Cadastro de Livros

## Sumário
1. [Introdução](#introdução)
2. [Requisitos do Sistema](#requisitos-do-sistema)
3. [Descrição das Funções](#descrição-das-funções)
4. [Fluxo de Execução](#fluxo-de-execução)
5. [Exemplo de Uso](#exemplo-de-uso)
6. [Conclusão](#conclusão)

## Introdução
O sistema foi desenvolvido para armazenar informações de livros utilizando filtros de entradas e um banco de dados integrado ao código. Este documento visa fornecer uma visão geral do sistema, incluindo a estrutura do código, a descrição das funções e um exemplo de uso.

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)
![SQLite Logo](https://www.sqlite.org/images/sqlite370_banner.gif)

## Requisitos do Sistema
- Python 3.x
- Biblioteca SQLite3

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
#          Saída esperada no console ao adicionar um livro:

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
