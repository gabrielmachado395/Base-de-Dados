import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()
# É uma boa prática de programação fechar após usar.

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'             # INTEGER == Int(no Python)
#                'nome TEXT,'                                        # TEXT == Str(no Python)
#                'peso REAL,'                                        # REAL == Bool(no Python)
#                'idade INTEGER'
#                ')')

# cursor.execute(
#    'INSERT INTO clientes (nome, peso, idade) VALUES (?, ?, ?)', 
#    ('Maria', 50, 23)
# )

# cursor.execute(
#    'INSERT INTO clientes (nome, peso, idade) VALUES (:nome, :peso, :idade)', 
#    {'nome': 'Pedro', 'peso': 93.8, 'idade': 19}
# )

# cursor.execute(
#    'INSERT INTO clientes VALUES (:id, :nome, :peso, :idade)',
#    {'id': None, 'nome': 'Daniel', 'peso': 70, 'idade': 25}
#)
# Adicionar os valores em si em 'VALUES' pode causar Sql Injection.
# Acima foram colocadas formas seguras de inserir valores em uma base de dados.

# conexao.commit()
# Adiciona as atlerações na base de dados.           

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Joana', 'id': 5}
# )

cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    # PELO AMOR DE DEUS NÂO COMETA O FAMOSO DELETE SEM WHERE.
    {'id': 2},
)
conexao.commit()



cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    indetificador, nome, peso, idade = linha

    print(linha)



cursor.close()
conexao.close()
# Talvez seja melhor escrever antes mesmo de adicionar códigos..