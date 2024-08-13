def mostrar(cursor,conexao):
    #cursor,conexao=conectar()
    cursor.execute(" select * from livro")
    print("ID               Livro                       Preço        Ano")
    for row in cursor.fetchall():
        linha =row
        if linha:
            
            print(f'{linha[0]:<8}   {linha[1]:<12} {linha[2]:<20} {linha[3]:>5}')
        
        
    print("gravados")
    cursor.close()
    conexao.close()  