import mariadb
import sys

class UsuarioModel:
    def __init__(self, db_name='jhedder_db', user='root', password='', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
       
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chefes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                fase VARCHAR(100),
                poder VARCHAR(100)
            )
        ''')
        self.conn.commit()

    def inserir_chefe(self,nome, fase, poder):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO chefes (nome, fase, poder) VALUES (?, ?, ?)', (nome, fase, poder))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao inserir chefe: {e}")

    def selecionar_chefe(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM chefes')
        return cursor.fetchall()

    def deletar_chefe(self, id):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM chefes WHERE id = ?
        ''', (id,))
        self.conn.commit()
    def atualizar_chefe(self,id,nome,fase, poder):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE chefes
            SET nome = ?, fase = ?, poder = ?
            WHERE id = ?
        ''',(nome,fase,poder, id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

