

CREATE TABLE realizar_orcamento (
Codigo int not null auto_increment,
Nome_Produto varchar(100) not null,
Frete DOUBLE NOT NULL,
Unidade int(50) NOT NULL ,
Qtd int(3) NOT NULL,
Desconto DOUBLE NOT NULL,
Preco_uni DOUBLE NOT NULL,
Preco_total DOUBLE NOT NULL,
Descrição_Produto longtext,
primary key(codigo)
); 


