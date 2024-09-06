-- Instruções
-- 1. No MySQL Workbench, crie o banco de dados 'sprint':
-- Escreva e execute os comandos para:
-- Criar a tabela chamada Atleta para conter os dados: idAtleta (int e chave primária da
-- tabela), nome (varchar, tamanho 40), modalidade (varchar, tamanho 40), qtdMedalha
-- (int, representando a quantidade de medalhas que o atleta possui)
-- Inserir dados na tabela, procurando colocar mais de um atleta para cada modalidade
-- e pelo menos 5 atletas.
-- Escreva e execute os comandos para:
-- • Exibir todos os dados da tabela.
-- • Atualizar a quantidade de medalhas do atleta com id=1;
-- • Atualizar a quantidade de medalhas do atleta com id=2 e com o id=3;
-- • Atualizar o nome do atleta com o id=4;
-- • Adicionar o campo dtNasc na tabela, com a data de nascimento dos atletas, tipo date;
-- • Atualizar a data de nascimento de todos os atletas;
-- • Excluir o atleta com o id=5;
-- • Exibir os atletas onde a modalidade é diferente de natação;
-- • Exibir os dados dos atletas que tem a quantidade de medalhas maior ou igual a 3;
-- • Modificar o campo modalidade do tamanho 40 para o tamanho 60;
-- • Descrever os campos da tabela mostrando a atualização do campo modalidade;
-- • Limpar os dados da tabela;

DROP DATABASE IF EXISTS sprint;
CREATE DATABASE IF NOT EXISTS sprint;
USE sprint;

CREATE TABLE Modalidade(
    idModalidade int primary key auto_increment,
    modalidade varchar(40)
);

CREATE TABLE Atleta(
    idAtleta int primary key auto_increment,
    nome varchar(40),
    idModalidade int,
    qtdMedalha int,
    foreign key fk_modalidade(idModalidade) references Modalidade(idModalidade) 
    ON DELETE SET NULL
    ON UPDATE CASCADE
);


-- Inserir dados na tabela, procurando colocar mais de um atleta para cada modalidade e pelo menos 5 atletas.
INSERT INTO Modalidade (modalidade) VALUES
('100 metros rasos'),
('Natação'),
('Salto em altura');

-- Inserir 5 atletas para a modalidade '100 metros rasos'
INSERT INTO Atleta (nome, idModalidade, qtdMedalha) VALUES
('Atleta A', 1, 3),
('Atleta B', 1, 1),
('Atleta C', 1, 2),
('Atleta D', 1, 4),
('Atleta E', 1, 0);

-- Inserir 5 atletas para a modalidade 'Natação'
INSERT INTO Atleta (nome, idModalidade, qtdMedalha) VALUES
('Atleta F', 2, 2),
('Atleta G', 2, 5),
('Atleta H', 2, 1),
('Atleta I', 2, 0),
('Atleta J', 2, 3);

-- Inserir 5 atletas para a modalidade 'Salto em altura'
INSERT INTO Atleta (nome, idModalidade, qtdMedalha) VALUES
('Atleta K', 3, 4),
('Atleta L', 3, 2),
('Atleta M', 3, 5),
('Atleta N', 3, 1),
('Atleta O', 3, 3);


-- • Exibir todos os dados da tabela.
SELECT
    *
FROM
    Atleta A
JOIN
    Modalidade M ON A.idModalidade = M.idModalidade;

-- • Atualizar a quantidade de medalhas do atleta com id=1;
UPDATE Atleta SET qtdMedalha = 4 where idAtleta = 1;

-- • Atualizar a quantidade de medalhas do atleta com id=2 e com o id=3;
UPDATE Atleta SET qtdMedalha = 3 where idAtleta in (2,3);

-- • Atualizar o nome do atleta com o id=4;
UPDATE Atleta SET nome = 'Atleta 4' where idAtleta = 4;

-- • Adicionar o campo dtNasc na tabela, com a data de nascimento dos atletas, tipo date;
ALTER TABLE Atleta ADD COLUMN dtNasc date after nome;

-- • Atualizar a data de nascimento de todos os atletas;
-- Atualizar a data de nascimento para a modalidade '100 metros rasos'
UPDATE Atleta SET dtNasc = '1990-01-15' WHERE nome = 'Atleta A';
UPDATE Atleta SET dtNasc = '1992-03-22' WHERE nome = 'Atleta B';
UPDATE Atleta SET dtNasc = '1988-07-30' WHERE nome = 'Atleta C';
UPDATE Atleta SET dtNasc = '1991-11-05' WHERE nome = 'Atleta 4';
UPDATE Atleta SET dtNasc = '1993-09-12' WHERE nome = 'Atleta E';

-- Atualizar a data de nascimento para a modalidade 'Natação'
UPDATE Atleta SET dtNasc = '1989-02-25' WHERE nome = 'Atleta F';
UPDATE Atleta SET dtNasc = '1990-12-10' WHERE nome = 'Atleta G';
UPDATE Atleta SET dtNasc = '1985-08-14' WHERE nome = 'Atleta H';
UPDATE Atleta SET dtNasc = '1992-04-07' WHERE nome = 'Atleta I';
UPDATE Atleta SET dtNasc = '1991-10-19' WHERE nome = 'Atleta J';

-- Atualizar a data de nascimento para a modalidade 'Salto em altura'
UPDATE Atleta SET dtNasc = '1986-06-18' WHERE nome = 'Atleta K';
UPDATE Atleta SET dtNasc = '1989-11-11' WHERE nome = 'Atleta L';
UPDATE Atleta SET dtNasc = '1994-01-22' WHERE nome = 'Atleta M';
UPDATE Atleta SET dtNasc = '1987-08-27' WHERE nome = 'Atleta N';
UPDATE Atleta SET dtNasc = '1990-05-16' WHERE nome = 'Atleta O';


-- • Excluir o atleta com o id=5;
DELETE FROM Atleta WHERE idAtleta = 5;

-- • Exibir os atletas onde a modalidade é diferente de natação;
SELECT
    *
FROM
    Atleta A
JOIN
    Modalidade M ON A.idModalidade = M.idModalidade
WHERE M.modalidade <> 'Natação';

-- • Exibir os dados dos atletas que tem a quantidade de medalhas maior ou igual a 3;
SELECT
    *
FROM
    Atleta A
JOIN
    Modalidade M ON A.idModalidade = M.idModalidade
WHERE A.qtdMedalha >= 3;

-- • Modificar o campo modalidade do tamanho 40 para o tamanho 60;
ALTER TABLE Modalidade MODIFY modalidade varchar(60);

-- • Descrever os campos da tabela mostrando a atualização do campo modalidade;
DESCRIBE Modalidade;

-- • Limpar os dados da tabela;
SET foreign_key_checks = 0;
TRUNCATE Atleta;
TRUNCATE Modalidade;
SET foreign_key_checks = 1;
SELECT * FROM Atleta;
SELECT * FROM Modalidade;