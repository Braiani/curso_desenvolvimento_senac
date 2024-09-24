drop database if exists banco;
create database if not exists banco;
use banco;

create table estados (
    id_estado int auto_increment primary key,
    nome_estado varchar(255),
    sigla varchar(3)
);

create table cidades (
    id_cidade int auto_increment primary key,
    nome_cidade varchar(255),
    id_estado int not null,
    foreign key fk_estado(id_estado) references estados(id_estado)
);

create table generos (
    id_genero int auto_increment primary key,
    nome_genero varchar(255)
);

create table racas (
    id_raca int auto_increment primary key,
    nome_raca varchar(255)
);

create table religioes (
    id_religiao int auto_increment primary key,
    nome_religiao varchar(255)
);

create table agencias (
    id_agencia int auto_increment primary key,
    endereco varchar(200) not null,
    id_cidade int not null,
    foreign key fk_cidade(id_cidade) references cidades(id_cidade)
);

create table clientes (
    id_cliente int auto_increment primary key,
    nome_cliente varchar(200) not null,
    cpf varchar(11) not null unique,
    rg varchar(15) not null,
    data_nascimento date not null,
    telefone varchar(30) not null,
    endereco varchar(200) not null,
    id_cidade int not null,
    numero_conta varchar(11) not null,
    id_agencia int not null,
    saldo float default 0,
    id_genero int not null,
    id_raca int not null,
    id_religiao int not null,

    foreign key fk_cidade(id_cidade) references cidades(id_cidade),
    foreign key fk_agencia(id_agencia) references agencias(id_agencia),
    foreign key fk_genero(id_genero) references generos(id_genero),
    foreign key fk_raca(id_raca) references racas(id_raca),
    foreign key fk_religiao(id_religiao) references religioes(id_religiao)
);

create table saques (
    id_saque int auto_increment primary key,
    id_agencia int not null,
    id_cliente int not null,
    valor_saque float not null,

    foreign key fk_agencia(id_agencia) references agencias(id_agencia),
    foreign key fk_cliente(id_cliente) references clientes(id_cliente)
);

create table depositos (
    id_deposito int auto_increment primary key,
    id_agencia int not null,
    id_cliente int not null,
    valor_deposito float not null,

    foreign key fk_agencia(id_agencia) references agencias(id_agencia),
    foreign key fk_cliente(id_cliente) references clientes(id_cliente)
);


-- Populando o Banco de dados antes das Triggers

-- Inserindo estados
INSERT INTO estados (nome_estado, sigla) VALUES 
('São Paulo', 'SP'),
('Rio de Janeiro', 'RJ'),
('Mato Grosso do Sul', 'MS'),
('Bahia', 'BA'),
('Rio Grande do Sul', 'RS');

-- Inserindo cidades
INSERT INTO cidades (nome_cidade, id_estado) VALUES 
('São Paulo', 1),
('Rio de Janeiro', 2),
('Campo Grande', 3),
('Salvador', 4),
('Porto Alegre', 5);

-- Inserindo gêneros
INSERT INTO generos (nome_genero) VALUES 
('Masculino'),
('Feminino'),
('Não-binário');

-- Inserindo raças
INSERT INTO racas (nome_raca) VALUES 
('Branca'),
('Parda'),
('Preta'),
('Amarela'),
('Indígena');

-- Inserindo religiões
INSERT INTO religioes (nome_religiao) VALUES 
('Cristianismo'),
('Espiritismo'),
('Islamismo'),
('Budismo'),
('Ateísmo');

-- Inserindo agências
INSERT INTO agencias (endereco, id_cidade) VALUES 
('Avenida Paulista, 1000', 1),
('Rua 7 de Setembro, 500', 2),
('Avenida Afonso Pena, 200', 3),
('Rua das Flores, 150', 4),
('Praça da Alfândega, 80', 5);

-- Inserindo clientes
INSERT INTO clientes (nome_cliente, cpf, rg, data_nascimento, telefone, endereco, id_cidade, numero_conta, id_agencia, saldo, id_genero, id_raca, id_religiao) VALUES 
('João Silva', '12345678901', '1234567', '1990-01-15', '31987654321', 'Rua das Acácias, 10', 1, '0000012345', 1, 1000.50, 1, 1, 1),
('Maria Oliveira', '23456789012', '2345678', '1985-02-20', '21987654321', 'Rua das Palmeiras, 20', 2, '0000023456', 2, 1500.75, 2, 2, 1),
('Carlos Pereira', '34567890123', '3456789', '1992-03-30', '31987654322', 'Rua das Orquídeas, 30', 3, '0000034567', 3, 2000.00, 1, 3, 2),
('Ana Santos', '45678901234', '4567890', '1988-04-05', '21987654323', 'Rua das Rosas, 40', 4, '0000045678', 4, 500.00, 2, 4, 3),
('Lucas Lima', '56789012345', '5678901', '1995-05-12', '31987654324', 'Rua das Margaridas, 50', 5, '0000056789', 5, 750.25, 1, 5, 4);

SELECT 
    c.nome_cliente,
    c.numero_conta,
    a.id_agencia,
    c.saldo
FROM 
    clientes c
JOIN 
    agencias a ON c.id_agencia = a.id_agencia;

delimiter $

create trigger adicionar_saldo after insert on depositos
for each row
begin
    update clientes set saldo = saldo + new.valor_deposito where clientes.id_cliente = new.id_cliente;
end$

delimiter ;

delimiter $

create trigger retirada_saldo before insert on saques
for each row
begin
    declare saldo_atual float;

    SELECT saldo into saldo_atual
    FROM clientes
    where clientes.id_cliente = new.id_cliente;

    IF saldo_atual < new.valor_saque then
        SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "Saldo insuficiente para realizar essa operação";
    end if;

    update clientes set saldo = saldo - new.valor_saque where clientes.id_cliente = new.id_cliente;

end$

delimiter ;

insert into depositos (id_agencia, id_cliente, valor_deposito) values (1,1,100);
insert into saques (id_agencia, id_cliente, valor_saque) values (3,3,2001);