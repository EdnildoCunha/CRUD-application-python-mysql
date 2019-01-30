create database SGP;
use SGP;
create table Fornecedor (
  Cod_Forn int not null auto_increment,
  Nome_Forn varchar(40) not null,
  End_Forn varchar(50) not null,
  primary key (Cod_Forn)
);

create table Cliente (
Cod_Cliente int not null auto_increment,
Nome_Cliente varchar(40) not null,
Cidade_Cliente varchar(40) not null,
primary key (Cod_Cliente)
);

create table Produto(
Cod_Produto int not null auto_increment,
Nome_Produto varchar(50) not null,
Unid_Produto varchar(10) not null,
Valor_Unit decimal(10,2) not null,
primary key (Cod_Produto)
);

create table Pedido(
Cod_Pedido int not null auto_increment,
Data_Entrega date,
Cod_Cliente int not null,
Cod_Forn int not null,
Cod_Produto int not null,
Qntd_Produto int not null,
primary key(Cod_Pedido),
foreign key(Cod_Cliente) references Cliente (Cod_Cliente),
foreign key(Cod_Forn) references Fornecedor (Cod_Forn),
foreign key(Cod_Produto) references Produto (Cod_Produto)
);


select * from Cliente;
select * from Fornecedor;
select * from Produto;
Select* from Pedido;
