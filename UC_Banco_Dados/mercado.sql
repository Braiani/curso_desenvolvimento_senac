DROP DATABASE IF EXISTS mercado;
CREATE DATABASE IF NOT EXISTS mercado;
USE mercado;

CREATE TABLE fornecedores(
    cod_forne varchar(50) NOT NULL UNIQUE PRIMARY KEY,
    nome varchar(255) NOT NULL,
    cidade_sede varchar(100) NOT NULL,
    grupo_cod_fornecedor varchar(100)
);

CREATE TABLE material(
    cod_material int auto_increment PRIMARY KEY,
    cod_fornecedor varchar(50) not null,
    nome varchar(255) NOT NULL,
    descricao varchar(255) NOT NULL,
    foreign key fk_fornecedor(cod_fornecedor) references fornecedores(cod_forne)
);

INSERT INTO fornecedores (cod_forne, nome, cidade_sede, grupo_cod_fornecedor) VALUES 
("ABC", "ABC Materiais Eletricos", "Vitoria", NULL ),
("XYZ", "XYZ Materiais de Escritorio", "Rio de Janeiro", "HiX"),
("Hidra", "Hidra Materiais Hidraulicos", "Sao Paulo", "HiX"),
("HiX", "HidraX Materiais ElÈtricos e Hidraulicos", "Sao Paulo", NULL);

INSERT INTO material (cod_material, cod_fornecedor, nome, descricao) VALUES 
(123, "ABC", "Tomada eletrica 10A Nova", "Tomada eletrica 10A padrao novo"),
(234, "ABC", "Disjuntor 25A", "Disjuntor eletrico 25A"),
(345, "XYZ", "Resma Papel A4", "Resma papel branco A4"),
(456, "XYZ", "Toner Imp HR5522", "Toner impressora HR5522"),
(678, "Hidra", "Cano PVC 1/2", "Cano PVC 1/2 pol"),
(679, "Hidra", "Cano PVC 3/4", "Cano PVC 3/4 pol"),
(680, "Hidra", "Medidor hidr 1/2", "Medidor hidraulico 1/2 pol"),
(681, "Hidra", "Joelho 1/2", "Conector Joelho 1/2 pol"),
(682, "Hidra", "Junta 1/2", "Cano PVC 1/2 pol"),
(1234, "ABC", "Tomada eletrica 20A Nova", "Tomada eletrica 20A padrao novo"),
(2345, "XYZ", "Caneta Azul", "Caneta esferografica azul"),
(4567, "XYZ", "Grapeador", "Grampeador mesa pequeno"),
(4568, "XYZ", "Caneta Marca Texto Amarela", "Caneta Marca Texto Amarela"),
(4569, "XYZ", "Lapis HB", "Lapis Preto H");

-- Crie o banco de dados com os registros acima e faça um Join entre as duas tabelas.
SELECT 
    *
FROM
    material m
        JOIN
    fornecedores f ON m.cod_fornecedor = f.cod_forne;

-- Quantos materiais possuem o Fornecedor ABC;
SELECT 
    count(*)
FROM
    material m
        JOIN
    fornecedores f ON m.cod_fornecedor = f.cod_forne
where
    m.cod_fornecedor = "ABC";

-- Quantos materiais possuem o Fornecedor XYZ;
SELECT 
    count(*)
FROM
    material m
        JOIN
    fornecedores f ON m.cod_fornecedor = f.cod_forne
where
    m.cod_fornecedor = "XYZ";

-- Quantos materiais possuem o Fornecedor HYDRA;
SELECT 
    count(*)
FROM
    material m
        JOIN
    fornecedores f ON m.cod_fornecedor = f.cod_forne
where
    m.cod_fornecedor = "Hidra";