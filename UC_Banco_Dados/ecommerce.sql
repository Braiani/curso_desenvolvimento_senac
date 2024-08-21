create database ecommerce; -- Typo na palavra database (datbase|database)
use ecommerce; -- Typo na palavra use (user|use)

---------------------------------------------

create table  produtos( -- Falta de abertura de parenteses
    id_prod int(5) auto_increment not null, -- Typo na palavra auto_increment (auto_incremento|auto_increment)
    nome_prod varchar(100) not null,
    descricao text, -- Falta de vírgula
    modelo varchar(50),
    id_categoria int(5), -- Falta de vírgula
    id_fabricante int(5),
    constraint primary key (id_prod) -- faltou a definição de uma primary key
);

   
create table clientes ( -- Typo na palavra table (tabela|table)
    id_cli int(5) auto_increment not null, -- Falta do _ na palavra id_cli e coluna com auto_increment deve ser inteiro
    nome varchar(100) not null,
    cpf int(11),
    telefone varchar(50),
    sexo enum('F','M'), -- Falta de vírgula
    cadastro datetime, -- Typo na palavra datetime (datestime|datetime)
    constraint primary key (id_cli) -- Typo na palavra primary (primari|primary)
); -- Identação - Não é erro, mas pelas boas práticas para facilitação de visualização do código

create table pedidos(
    num_pedido int(5) auto_increment not null,
    data datetime,
    status varchar(50),
    id_cli int(5), -- Espaços ao invés de tab
    constraint primary key (num_pedido),
    constraint foreign key (id_cli) references clientes(id_cli)
);

   
create table pedido_item( -- Typo na palavra table (tabe|table)
    idtem_pedido int(5) auto_increment not null,
    num_pedido int(5) not null,
    qtde int(5) not null,
    valor_unit decimal(10,2),
    total decimal(10,2),
    id_prod int(5),
    constraint primary key (idtem_pedido),
    constraint foreign key (num_pedido) references pedidos(num_pedido), -- Typo na palavra foreign (foreing|foreign)
    constraint foreign key (id_prod) references produtos(id_prod) -- Typo na palavra foreign (foreing|foreign)
); -- Identação - Não é erro, mas pelas boas práticas para facilitação de visualização do código

create table estoque_produtos(
    id_estoque int(5) auto_increment not null, -- Falta informação do auto_increment e not null
    quantidade int(5) not null,
    quant_min int(5),
    id_prod int(5), -- Falta fechar parenteses
    constraint primary key (id_estoque),
    constraint foreign key (id_prod) references produtos(id_prod)
);

insert into clientes values (null,'João','02102202324','6799999999','M',now()); -- falta s no nome da tabela
insert into clientes values (null,'Tadeu','02102202366','6799999999','M',now()); -- falta r na palavra insert
insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());
insert into clientes values (null,'Maria','02102202377','6799999999','F',now());
insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());

insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);

insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null,null); -- Falta aspas na palavra Processador AMD e falta de vígula entre null


insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null,null); -- Falta aspas na palavra CX1200W e falta de vígula entre null

   
select * from produtos; -- Typo na palavra from (form|from)
describe estoque_produtos; -- Typo na palavra describe (describle|describe)


insert into estoque_produtos values (null,80,10,1);
insert into estoque_produtos values (null,44,5,9); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,55,5,8); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,36,5,7); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,49,5,6); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,100,5,1); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,100,5,2); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,100,5,3); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,100,5,4); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)
insert into estoque_produtos values (null,100,5,5); -- Typo na palavra into (int|into) | Falta de s no nome da tabela | typo na palavra values (valuer|values)