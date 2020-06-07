
import sqlite3

banco = sqlite3.connect('cadastroProdutos.db')

cursor = banco.cursor()


cursor.execute("drop table usuario_produto")
cursor.execute("drop table produto")
cursor.execute("drop table usuario")
cursor.execute("drop table intencao")
cursor.execute("drop table marca")


