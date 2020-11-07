Create table compra (
id int auto_increment,
nome varchar (100) not null,
ean varchar(30) not null,
preco double not null,
qtd int not null,
forma_pg varchar (100) not null,
primary key (id) );

select* from compra
