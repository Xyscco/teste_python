import fdb
# from core.database_connection import conectar_banco

consulta = "SELECT * FROM PRODUTO"

def conectar_banco(tipo_banco, nome_banco, porta=None):
    # Função fictícia para simular a conexão com o banco de dados
    if tipo_banco == 'firebird':
        return fdb.connect(
                host='localhost',
                port=porta,
                database=nome_banco,
                user='SYSDBA',
                password='masterkey',
                charset='WIN1252'
            )
    else:
        raise ValueError("Tipo de banco não suportado")

try:
    conexao = conectar_banco('firebird', '/firebird/data/unifar.fdb', porta=3050)
    print('Conexão estabelecida com sucesso')

    cursor = conexao.cursor()
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    print(f"Resultados da consulta: {resultados}")
except Exception as e:
    print(f"Erro: {e}")