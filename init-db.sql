select produto.id, produto.nome, marca.nome, produto."nomeImagem"
from
    main.doabetesite_produto produto,
    main.doabetesite_marca marca,
    main.doabetesite_marcaproduto mp
where produto.id = mp.produto_id
    and marca.id = mp.marca_id;

select distinct nome, count (nome) from main.doabetesite_produto having count nome > 1

--apagar resgistro
delete from main.doabetesite_marcaproduto;
delete from main.doabetesite_produto;
delete from main.doabetesite_marca;


-- insert tabela marca
--marcas Aparelho medidor de glicose
insert into main.doabetesite_produto (nome, nomeImagem) values ('Aparelho medidor de glicose', 'static/img/produto_imagem/aparelho.png');
insert into main.doabetesite_marca (nome) values ('Accu check active');
insert into main.doabetesite_marca (nome) values ('Accu check performa');
insert into main.doabetesite_marca (nome) values ('Breeze 2');
insert into main.doabetesite_marca (nome) values ('Freestyle lite');
insert into main.doabetesite_marca (nome) values ('One touch select simple');
insert into main.doabetesite_marca (nome) values ('One touch ultra');
insert into main.doabetesite_marca (nome) values ('One touch ultra mini');

insert into main.doabetesite_marcaproduto  (produto_id, marca_id) select (select produto.id from main.doabetesite_produto produto where produto.nome ='Aparelho medidor de glicose'), marca.id from main.doabetesite_marca marca where marca.nome  in ('Accu check active', 'Accu check performa','Breeze 2', 'Freestyle lite', 'One touch select simple', 'One touch ultra', 'One touch ultra mini'),



-- marcas insulina
insert into main.doabetesite_produto (nome, nomeImagem) values ('Insulina', 'static/img/produto_imagem/insulina.png');

insert into main.doabetesite_marca (nome) values ('Levemir');
insert into main.doabetesite_marca (nome) values ('Tresiba');
insert into main.doabetesite_marca (nome) values ('Lantus');
insert into main.doabetesite_marca (nome) values ('Novolin N');
insert into main.doabetesite_marca (nome) values ('Humulin N');
insert into main.doabetesite_marca (nome) values ('Humulin L');
insert into main.doabetesite_marca (nome) values ('Novolin L');
insert into main.doabetesite_marca (nome) values ('Humalog Mix');
insert into main.doabetesite_marca (nome) values ('Novorapid');

insert into main.doabetesite_marcaproduto  (produto_id, marca_id) select (select produto.id from main.doabetesite_produto produto where produto.nome ='Insulina'), marca.id from main.doabetesite_marca marca where marca.nome  in ('Levemir','Tresiba','Lantus','Novolin N','Humulin N','Humulin L','Novolin L','Humalog Mix','Novorapid');


--marcas Insumos de bomba de insulina
insert into main.doabetesite_produto (nome, nomeImagem) values ('Catéter', 'static/img/produto_imagem/bomba.png');
insert into main.doabetesite_produto (nome, nomeImagem) values ('Aplicadores', 'static/img/produto_imagem/orto.png');
insert into main.doabetesite_produto (nome, nomeImagem) values ('Reservatório', 'static/img/produto_imagem/caneta.png');

insert into main.doabetesite_marca (nome) values ('Medtronic');
insert into main.doabetesite_marca (nome) values ('Roche');
insert into main.doabetesite_marca (nome) values ('MicroPort');
insert into main.doabetesite_marca (nome) values ('Deka');
insert into main.doabetesite_marca (nome) values ('IACollaborative');

insert into main.doabetesite_marcaproduto  (produto_id, marca_id) select (select produto.id from main.doabetesite_produto produto where produto.nome ='Catéter'), marca.id from main.doabetesite_marca marca where marca.nome  in ('Medtronic','Roche','MicroPort','Deka','IACollaborative');

 insert into main.doabetesite_marcaproduto  (produto_id, marca_id) select (select produto.id from main.doabetesite_produto produto where produto.nome ='Aplicadores'),marca.id from main.doabetesite_marca marca where marca.nome  in ('Medtronic','Roche','MicroPort','Deka','IACollaborative');

 insert into main.doabetesite_marcaproduto  (produto_id, marca_id) select (select produto.id from main.doabetesite_produto produto where produto.nome ='Reservatório'),marca.id from main.doabetesite_marca marca where marca.nome  in ('Medtronic','Roche','MicroPort','Deka','IACollaborative');

commit










