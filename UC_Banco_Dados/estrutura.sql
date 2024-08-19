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