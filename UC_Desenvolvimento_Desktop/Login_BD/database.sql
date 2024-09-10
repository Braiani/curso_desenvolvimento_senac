CREATE DATABASE IF NOT EXISTS mercado;
USE mercado;

CREATE TABLE IF NOT EXISTS usuarios(
    id int auto_increment primary key,
    nome varchar(200) NOT NULL,
    usuario varchar(50) NOT NULL,
    senha varchar(255) NOT NULL,
    mensagem text,
    photo varchar(255)
);

INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Administrador', 'admin', md5('senha'), 'Sou o Administrador do Sistema!');