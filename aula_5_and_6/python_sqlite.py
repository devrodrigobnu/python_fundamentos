import sqlite3
import os


class BancoDeDados:
    @staticmethod
    def criar_conexao(nome_base):
        BancoDeDados.conexao = sqlite3.connect(nome_base)
        print('Conexão estabelecida com sucesso.')
        return BancoDeDados.conexao
    
    @staticmethod 
    def criar_tabela(nome_tabela_nova):
        cursor = BancoDeDados.conexao.cursor()

        sql_string = f''' 
            CREATE TABLE IF NOT EXISTS {nome_tabela_nova} (
                id INTEGER PRIMARY KEY,
                nome TEXT(40),
                numero TEXT(15),
                email TEXT(40)
            )
        '''

        cursor.execute(sql_string)
        BancoDeDados.conexao.commit()
        cursor.close()
        print(f'Tabela {nome_tabela_nova} criada com sucesso.')
    
    @staticmethod 
    def insere_dados(nome_tabela, nome_usuario, numero_usuario, email_usuario):
        cursor = BancoDeDados.conexao.cursor()

        sql_string = f"""
            INSERT INTO {nome_tabela}
                (nome, numero, email)
                VALUES ('{nome_usuario}', '{numero_usuario}', '{email_usuario}')
        """

        cursor.execute(sql_string)
        BancoDeDados.conexao.commit()
        cursor.close()
        print(f'Dados: {nome_usuario} - {numero_usuario} - {email_usuario} inseridos em {nome_tabela} com sucesso.')
    
    @staticmethod 
    def delete_linha(nome_tabela, id_linha):
        cursor = BancoDeDados.conexao.cursor()

        sql_query = f"""
            SELECT * FROM {nome_tabela}
            WHERE id = {id_linha}
        """

        cursor.execute(sql_query)
        resultado_sql = cursor.fetchall()

        if len(resultado_sql) > 0:
            sql_delete = f"""
                DELETE FROM {nome_tabela}
                WHERE ID = {id_linha}            
            """
            cursor.execute(sql_delete)
            BancoDeDados.conexao.commit()
            print(f'Linha {id_linha} deletada com sucesso.')
        else:
            print(f'Tabela {nome_tabela} com id {id_linha} não existe')
            cursor.close()
    
    @staticmethod 
    def mostra_tabela(nome_tabela):
        cursor = BancoDeDados.conexao.cursor()

        sql_query = f"""
            SELECT * FROM {nome_tabela}
        """

        cursor.execute(sql_query)
        rows = cursor.fetchall()
        
        if len(rows) > 0:
            print(f'Dados da tabela {nome_tabela}:\n')
            for row in rows:
                print(row)
                print('\n')    
                
        BancoDeDados.conexao.commit()
        cursor.close()
    
    @staticmethod 
    def atualiza_linha(id_linha, nome_tabela, nome_novo, numero_novo, email_novo):
        cursor = BancoDeDados.conexao.cursor()

        sql_update = f"""
            SELECT * FROM {nome_tabela}
            WHERE id = {id_linha}
        """
        cursor.execute(sql_update)
        resultado_sql = cursor.fetchall()
        
        if len(resultado_sql) > 0:
            sql_atualiza = f"""
                UPDATE {nome_tabela}
                SET nome = ?, numero = ?, email = ?
                WHERE id = ?
            """
            valores_atualizados = (nome_novo, numero_novo, email_novo, id_linha)
            cursor.execute(sql_atualiza, valores_atualizados)

            BancoDeDados.conexao.commit()
            print(f'Linha {id_linha} atualizada com sucesso.')
        else:
            print('Registro não encontrado')

        cursor.close()

    @staticmethod
    def valida_colunas_banco(nome, numero, email):
        
        valida_email = False    
        #### VALIDA EMAILS = Precisam ter @ e . em um Len de pelo menos 10 characteres
        if len(email) >= 10 and '@' in email and '.' in email:
            valida_email = True
        
        valida_nome = False
        #### VALIDA NOME = Precisa ter tres caracteres e não pode ter número
        numeros = ['1','2','3','4','5','6','7','8','9']
        if len(nome) >3:
            valida_nome = True

            for numero in numeros:
                if numero in nome:
                    valida_nome = False

        valida_numero = False
        #### VALIDA NUMERO = Só pode números e os símbolos: + () -
        lista_simbolos = ['()', ')', '-', '+']
        if len(numero) >= 8 and len(numero) <= 14:
            numeros_lista = list(numero)

            contador = 0
            for n in numeros_lista:
                if n in numeros or n in lista_simbolos:
                    if n in numeros:
                        contador += 1
                elif n not in numeros and n not in lista_simbolos:
                    contador = 0
                    break
            
            if contador >= 8:
                valida_numero = True     

        return valida_email and valida_nome and valida_numero
    
def database_manager():
    conn = BancoDeDados.criar_conexao('base_de_dados.db')

    menu_interface = '''
1 - Criar tabela
2 - Inserir dados
3 - Deletar linha
4 - Mostrar tabela
5 - Atualizar linha
6 - Sair
Insira a operação (1 - 6): '''
    
    while True:
        try:
            operacao = int(input(menu_interface))

            if operacao == 1:
                nome_tabela = input('Informe o nome da tabela nova: ')
                BancoDeDados.criar_tabela(nome_tabela)

            elif operacao == 2:
                tabela = input('Informe o nome da tabela: ')
                nome = input('Informe o nome do contato: ')
                numero = input('Informe o número do contato: ')
                email = input('Informe o e-mail do contato: ')
                dados_validos = BancoDeDados.valida_colunas_banco(nome, numero, email)
                if dados_validos is True:
                    BancoDeDados.insere_dados(
                    nome_tabela=tabela,
                    nome_usuario=nome,
                    numero_usuario=numero,
                    email_usuario=email
                )
                else:
                    print('Informe dados válidos!!')
            
            elif operacao == 3:
                tabela = input('Informe o nome da tabela: ')
                id_linha = input('Informe o ID da linha a ser deletada: ')
                BancoDeDados.delete_linha(tabela, id_linha)
                print(f'Linha {id_linha} deletada na tabela {tabela}.')

            elif operacao == 4:
                tabela = input('Informe o nome da tabela: ')
                BancoDeDados.mostra_tabela(tabela)

            elif operacao == 5:
                tabela = input('Informe o nome da tabela a ser alterada: ')
                id_linha = int(input("Digite o ID da linha a ser atualizada: "))
                nome_novo = input("Digite o novo nome: ")
                numero_novo = input("Digite o novo número: ")
                email_novo = input("Digite o novo email: ")
                BancoDeDados.valida_colunas_banco(nome, numero, email)
                BancoDeDados.atualiza_linha(id_linha, tabela, nome_novo, numero_novo, email_novo)

            elif operacao == 6:
                print('Programa encerrado.')
                break
            else:
                print('Informe uma operação válida!')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    conn.close()
    print('Conexão encerrada.')

if __name__ == '__main__':
    os.system('cls')
    database_manager()
