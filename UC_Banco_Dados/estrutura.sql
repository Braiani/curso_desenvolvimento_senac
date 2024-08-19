CREATE DATABASE estrutura;

USE estrutura;

CREATE TABLE EX2_CLIENTE(
    codcliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    datanascimento DATE NOT NULL,
    cpf VARCHAR(14) NOT NULL
);

CREATE TABLE EX2_PEDIDO(
    codpedido INT AUTO_INCREMENT PRIMARY KEY,
    codcliente INT NOT NULL,
    datapedido DATE NOT NULL,
    nf VARCHAR(200),
    valortotal FLOAT NOT NULL,
    FOREIGN KEY (codcliente) REFERENCES EX2_CLIENTE(codcliente)
);

CREATE TABLE EX2_PRODUTO(
    codproduto INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    quantidade INT
);

CREATE TABLE EX2_ITEMPEDIDO(
    codpedido INT NOT NULL,
    numeroitem INT AUTO_INCREMENT PRIMARY KEY,
    valorunitario FLOAT NOT NULL,
    quantidade INT NOT NULL,
    codproduto INT NOT NULL,
    FOREIGN KEY (codpedido) REFERENCES EX2_PEDIDO(codpedido),
    FOREIGN KEY (codproduto) REFERENCES EX2_PRODUTO(codproduto)
);

CREATE TABLE EX2_LOG(
    codlog INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

CREATE TABLE EX2_REQUISICAO_COMPRA(
    codrequisicaocompra INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    codproduto INT NOT NULL,
    data DATE NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (codproduto) REFERENCES EX2_PRODUTO(codproduto)
);

INSERT INTO EX2_CLIENTE (nome, datanascimento, cpf) VALUES 
    ('Cliente 01', '1990-05-25', '123.456.789-00'),
    ('Cliente 02', '1990-06-25', '123.456.789-01'),
    ('Cliente 03', '1990-07-25', '123.456.789-02'),
    ('Cliente 04', '1990-08-25', '123.456.789-03'),
    ('Cliente 05', '1990-09-25', '123.456.789-04'),
    ('Cliente 06', '1990-05-05', '123.456.789-05'),
    ('Cliente 07', '1990-06-15', '123.456.789-06'),
    ('Cliente 08', '1990-07-13', '123.456.789-07'),
    ('Cliente 09', '1990-08-15', '123.456.789-08'),
    ('Cliente 10', '1990-09-14', '123.456.789-09');
    
INSERT INTO EX2_PRODUTO (descricao, quantidade) VALUES 
    ('Produto 01', '5'),
    ('Produto 02', '6'),
    ('Produto 03', '7'),
    ('Produto 04', '8'),
    ('Produto 05', '9'),
    ('Produto 06', '5'),
    ('Produto 07', '6'),
    ('Produto 08', '7');

INSERT INTO EX2_PEDIDO (codcliente, datapedido, nf, valortotal) VALUES 
    (6,now(), '123G-12', 1520.6),
    (2,'2024-08-18', null, 125.6),
    (7,now(), '225F-G52', 632.5),
    (1,'2024-08-18', null, 1233.6),
    (3,'2024-08-18', null, 125.6);

INSERT INTO EX2_ITEMPEDIDO (codpedido, valorunitario, quantidade, codproduto) VALUES 
    (4,25.5, 3, 3),
    (2,22.3, 2, 4),
    (5,26.5, 7, 2),
    (1,40.5, 20, 1),
    (3,26, 5, 6);