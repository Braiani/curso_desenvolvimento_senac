CREATE DATABASE IF NOT EXISTS mercado_senac;
USE mercado_senac;

CREATE TABLE IF NOT EXISTS perfil(
    id int auto_increment primary key,
    nome varchar(200) NOT NULL,
    descricao text
);


CREATE TABLE IF NOT EXISTS usuarios(
    id int auto_increment primary key,
    nome varchar(200) NOT NULL,
    usuario varchar(50) NOT NULL,
    senha varchar(255) NOT NULL,
    mensagem text,
    photo varchar(255),
    perfil_id int,
    FOREIGN KEY (perfil_id) REFERENCES perfil(id)
);

INSERT INTO perfil(nome, descricao) values('Administrador', 'Perfil de Administrador do Sistema');
INSERT INTO perfil(nome, descricao) values('Usuario', 'Perfil de Usuário do Sistema');
INSERT INTO perfil(nome, descricao) values('Convidado', 'Perfil de Convidado do Sistema');

INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Administrador', 'admin', md5('senha'), 'Sou o Administrador do Sistema!');
INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Administrador 2', 'admin2', md5('senha'), 'Sou o Administrador do Sistema!');
INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Usuario', 'usuario', md5('senha'), 'Sou um Usuário do Sistema!');
INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Usuario 2', 'usuario2', md5('senha'), 'Sou um Usuário do Sistema!');
INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Convidado', 'convidado', md5('senha'), 'Sou um Convidado do Sistema!');
INSERT INTO usuarios(nome, usuario, senha, mensagem) values('Convidado 2', 'convidado2', md5('senha'), 'Sou um Convidado do Sistema!');