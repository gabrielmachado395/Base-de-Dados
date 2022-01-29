import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()
        # Aqui eu estou forçando a conexao fechar.


with conecta() as conexao:
    with conexao.cursor() as cursor:
       sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
             '(%s, %s, %s, %s)'
       cursor.execute(sql, ('Jack', 'Monroe', 115, 90))
       conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        # Esse with está sendo usado para fechar automaticamente o cursor.
        cursor.execute('SELECT * FROM clientes ORDER BY peso ASC LIMIT 100')
        # É uma boa prática de programação colocar limites nas pesquisas na base de dados.
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

