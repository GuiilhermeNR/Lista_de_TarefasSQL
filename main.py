import sqlite3
import re
num = 0

Conexao = sqlite3.connect('Banco_Dados.db')

Cursor = Conexao.cursor()

print("Lista de Tarefas")

nome_lista = str(input("Escolha o nome da sua lista de tarefas:")).strip()

Cursor.execute(f'CREATE TABLE IF NOT EXISTS "{nome_lista}" (num REAL, nome TEXT, status TEXT)')

Conexao.commit()

print("Tabela criada com sucesso!")

while True:

    print("""
    Oque deseja fazer com sua Lista de Tarefas
    [1] Adicionar Tarefa
    [2] Deletar Tarefa
    [3] Modificar Tarefa
    [4] Marcar Tarefa como Concluida
    [5] Encerrar Programa      
    """)
    escolha = int(input("Qual é a sua escolha?")) 

    if  escolha == 1:
        while True:

            nome_tarefa = str(input("Insira o Nome da Sua Tarefa:")).strip()
            num += 1
            Cursor.execute(f'INSERT INTO "{nome_lista}" VALUES (?, ?, ?)', (num, nome_tarefa, 'Pendente'))
            print("Tarefa Adicionada com Sucesso!")

            continuar = str(input("Deseja Adicionar mais Tarefas? [S/N]:")).strip().upper()
            if continuar == 'N':
                break
            else:
                print("Opção Inválida selecione uma opção válida")

    elif escolha == 2:

        Cursor.execute(f'SELECT COUNT(*) FROM "{nome_lista}"')
        quantidade = Cursor.fetchone()[0]

        if quantidade == 0:
            print("Ainda não existem tarefas adicionadas.")
        
        else:
            tarefas = Cursor.execute(f'SELECT * FROM "{nome_lista}"').fetchall()
            for tarefa in tarefas:
                print(tarefa)
            
            tarefa_id = int(input("Selecione o numero da terefa q deseja deletar:"))
            Cursor.execute(f'DELETE FROM "{nome_lista}" WHERE num = ?', (tarefa_id,))
            Conexao.commit()
            print("Tarefa deletada com sucesso!")

    elif escolha == 3:
        Cursor.execute(f'SELECT * FROM "{nome_lista}"')
        tarefas = Cursor.fetchall()

        if len(tarefas) == 0:
            print("Ainda não existem tarefas para modificar")
        else:
            print("Tarefas disponiveis")
            for tarefa in tarefas:
                print(tarefa)
        
        mod_tarefa = int(input("Selecione o numero da tarefa q deseja modificar"))
        novo_nome = str(input("Qual nome Deseja colocar ?:")).strip()
        
        Cursor.execute(f'UPDATE "{nome_lista}" SET nome = ? WHERE num  = ?', (novo_nome, mod_tarefa) )
        Conexao.commit()
        print("Tarefa modificada com sucesso!")

    elif escolha == 4:
        Cursor.execute(f'SELECT * FROM "{nome_lista}"')
        tarefas = Cursor.fetchall()

        if len(tarefas) == 0:
            print("Ainda não existem tarefas para marcar como concluidas")
        else:
            print("Tarefas disponiveis")
            for tarefa in tarefas:
                print(tarefa)
        con_tarefa = int(input("Qual o numero da tarefa que deseja marcar como concluida ?:"))

        Cursor.execute(f'UPDATE "{nome_lista}" SET status = ? WHERE num  = ?', ('Concluido', con_tarefa))
        Conexao.commit()
        print("Tarefa Marcada como Concluída com sucesso!")

    elif escolha == 5:
        print("Encerrando Programa...")
        break

    else:
        print("escolha uma opção válida")

            
        

