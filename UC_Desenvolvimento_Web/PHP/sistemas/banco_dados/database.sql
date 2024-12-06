create table users (
    id int auto_increment primary key,
    nome varchar(100),
    email varchar(100) NOT NULL,
    senha varchar(100) NOT NULL,
    is_admin tinyint default 0
);

INSERT INTO users(nome,email,senha,is_admin) VALUES ('Admin','admin@admin.com','1234',1);
INSERT INTO users(nome,email,senha,is_admin) VALUES ('Usuário','user@user.com','1234',1);