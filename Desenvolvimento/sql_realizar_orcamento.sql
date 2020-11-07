

CREATE TABLE realizar_orcamento (
Codigo int not null auto_increment,
Descrição_Produto VARCHAR(100) NOT NULL ,
Unidade int(50) NOT NULL ,
Qtd int(255) NOT NULL,
Preco_lista DOUBLE(10) NOT NULL,
Desconto DOUBLE(10) NOT NULL,
Preco_uni DOUBLE(10) NOT NULL,
Preco_total DOUBLE(10) NOT NULL,
Frete DOUBLE(10) NOT NULL,
primary key(codigo)
); 


