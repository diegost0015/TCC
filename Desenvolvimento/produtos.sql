create table produtos (
id int not null auto_increment,
Nome varchar (100) not null,
EAN int (3) not null,
Estoque varchar (10) not null,
Preco double not null,
Altura varchar (20),
Largura varchar (20),
Descricao longtext not null,
primary key (id));



