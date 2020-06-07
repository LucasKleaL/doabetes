
import sqlite3

banco = sqlite3.connect('cadastroProdutos.db')

cursor = banco.cursor()


cursor.execute("create table produto (id_produto INTEGER NOT NULL PRIMARY KEY, descricao text, id_marca integer, foreign key (id_marca) references marca(id_marca))")
cursor.execute("create table usuario (id_usuario INTEGER NOT NULL PRIMARY KEY, nome text)")
cursor.execute("create table marca (id_marca INTEGER NOT NULL PRIMARY KEY, descricao text)")
cursor.execute("create table intencao (id_intencao INTEGER NOT NULL PRIMARY KEY, descricao text)")
cursor.execute("create table usuario_produto (id_usuario INTEGER NOT NULL, id_produto INTEGER NOT NULL, id_intencao INTEGER NOT NULL, id_receptor integer, PRIMARY KEY(id_usuario, id_produto, id_intencao), foreign key (id_intencao) references intencao(id_intencao), foreign key (id_produto) references produto(id_produto), foreign key (id_usuario) references usuario(id_usuario), foreign key (id_receptor) references usuario(id_usuario))")

cursor.execute("INSERT INTO marca (id_marca, descricao) VALUES (1, 'marca 1')")
cursor.execute("INSERT INTO marca (id_marca, descricao) VALUES (2, 'marca 2')")

cursor.execute("INSERT INTO produto (id_produto, descricao, id_marca) VALUES (1, 'Aparelho medidor de glicose', 1)")
cursor.execute("INSERT INTO produto (id_produto, descricao, id_marca) VALUES (2, 'Tiras para medir glicose', 1)")
cursor.execute("INSERT INTO produto (id_produto, descricao, id_marca) VALUES (3, 'Insulina', 1)")
cursor.execute("INSERT INTO produto (id_produto, descricao, id_marca) VALUES (4, 'Seringas de aplicação', 1)")
cursor.execute("INSERT INTO produto (id_produto, descricao, id_marca) VALUES (5, 'Canetas de aplicação de insulina', 1)")
cursor.execute("INSERT INTO produto (id_produto, descricao, id_marca) VALUES (6, 'Insumos de bomba de infusão', 1)")

cursor.execute("INSERT INTO intencao (id_intencao, descricao) VALUES (1, 'doar')")
cursor.execute("INSERT INTO intencao (id_intencao, descricao) VALUES (2, 'receber')")


cursor.execute("INSERT INTO usuario (id_usuario, nome) VALUES (1, 'tiago')")
cursor.execute("INSERT INTO usuario (id_usuario, nome) VALUES (2, 'luiz')")
cursor.execute("INSERT INTO usuario (id_usuario, nome) VALUES (3, 'lenir')")
cursor.execute("INSERT INTO usuario (id_usuario, nome) VALUES (4, 'eduardo')")


