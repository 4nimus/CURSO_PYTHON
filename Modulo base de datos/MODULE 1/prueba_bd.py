import psycopg2

user = 'postgres'
password = '2311'
host = '127.0.0.1'
port = '5430'
database = 'test_db'

conexion = psycopg2.connect(user = user,
                            password = password,
                            host = host,
                            port = port,
                            database = database
                            )

cursor = conexion.cursor()
sentencia = 'select * from persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)