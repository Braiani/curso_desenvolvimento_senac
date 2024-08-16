create database netflix;
use netflix;
create table usuarios(
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    senha varchar(100) not null,
    data_nascimento date not null,
    cpf varchar(100) not null,
    telefone varchar(100),
    cadastro_ativo tinyint default 1
);
create table enderecos(
    id int primary key auto_increment,
    usuario_id int not null,
    rua varchar(100) not null,
    numero int not null,
    bairro varchar(100) not null,
    cidade varchar(100) not null,
    estado char(2) not null,
    cep varchar(100) not null,
    foreign key (usuario_id) references usuarios(id)
);
create table cartoes(
    id int primary key auto_increment,
    usuario_id int not null,
    endereco_id int not null,
    numero varchar(100) not null,
    nome_titular varchar(100) not null,
    data_validade date not null,
    cvv int not null,
    foreign key (usuario_id) references usuarios(id),
    foreign key (endereco_id) references enderecos(id)
);
create table planos(
    id int primary key auto_increment,
    nome varchar(100) not null,
    valor float not null,
    duracao int default 30
);
create table assinaturas(
    id int primary key auto_increment,
    usuario_id int not null,
    plano_id int not null,
    data_inicio date not null,
    data_fim date not null,
    foreign key (usuario_id) references usuarios(id),
    foreign key (plano_id) references planos(id)
);
create table situacao_pagamento(
    id int primary key auto_increment,
    descricao varchar(100) not null
);
create table avisos_emails(
    id int primary key auto_increment,
    usuario_id int not null,
    data date not null,
    assunto varchar(100) not null,
    mensagem text not null,
    foreign key (usuario_id) references usuarios(id)
);
create table pagamentos(
    id int primary key auto_increment,
    usuario_id int not null,
    data date not null,
    valor float not null,
    situacao_id int not null,
    cartao_id int not null,
    avisos_email_id int,
    foreign key (usuario_id) references usuarios(id),
    foreign key (situacao_id) references situacao_pagamento(id),
    foreign key (cartao_id) references cartoes(id),
    foreign key (avisos_email_id) references avisos_emails(id)
);
create table produtoras (
    id int primary key auto_increment,
    nome varchar(100) not null,
    data_fundacao date not null,
    cidade_sede varchar(100) not null
);
create table filmes (
    id int primary key auto_increment,
    duracao int not null
);
create table series (
    id int primary key auto_increment,
    temporadas int not null
);
create table documentarios (
    id int primary key auto_increment,
    duracao int not null,
    produtora_id int not null,
    foreign key (produtora_id) references produtoras(id)
);
create table videos (
    id int primary key auto_increment,
    titulo varchar(100) not null,
    ano_producao int not null,
    caminho_arquivo varchar(255) not null,
    tipo_video enum("f","s","d") default "f",
    filme_id int,
    serie_id int,
    documentario_id int,
    foreign key (filme_id) references filmes(id),
    foreign key (serie_id) references series(id),
    foreign key (documentario_id) references documentarios(id)
);
create table episodios (
    id int primary key auto_increment,
    serie_id int not null,
    titulo varchar(100) not null,
    ano_producao int not null,
    duracao int not null,
    temporada int not null,
    numero int not null,
    proximo_episodio_id int,
    foreign key (proximo_episodio_id) references episodios(id),
    foreign key (serie_id) references series(id)
);
create table avaliacoes (
    id int primary key auto_increment,
    usuario_id int not null,
    nota int not null,
    foreign key (usuario_id) references usuarios(id)
);
create table atores (
    id int primary key auto_increment,
    nome varchar(100) not null,
    data_nascimento date not null,
    local_nascimento varchar(100) not null
);
create table atores_videos (
    ator_id int not null,
    video_id int not null,
    foreign key (ator_id) references atores(id),
    foreign key (video_id) references videos(id)
);
create table assistidos (
    usuario_id int not null,
    video_id int not null,
    avaliacao_id int,
    foreign key (video_id) references videos(id),
    foreign key (avaliacao_id) references avaliacoes(id),
    foreign key (usuario_id) references usuarios(id)
);