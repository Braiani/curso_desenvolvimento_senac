-- ===========================================  ATIVIDADE 01 ===================================================== --
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

-- =========================================== END ATIVIDADE 01 ===================================================== --

-- ===========================================  ATIVIDADE 02 ===================================================== --
-- 2. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Criar a tabela chamada Musica para conter os dados: idMusica, titulo (tamanho 40), artista
-- (tamanho 40), genero (tamanho 40), sendo que idMusica é a chave primária da tabela.
-- Inserir dados na tabela, procurando colocar um gênero de música que tenha mais de uma
-- música, e um artista, que tenha mais de uma música cadastrada. Procure inserir pelo
-- menos umas 7 músicas.
-- Execute os comandos para:
-- a) Exibir todos os dados da tabela.
-- b) Adicionar o campo curtidas do tipo int na tabela;
-- c) Atualizar o campo curtidas de todas as músicas inseridas;
-- d) Modificar o campo artista do tamanho 40 para o tamanho 80;
-- e) Atualizar a quantidade de curtidas da música com id=1;
-- f) Atualizar a quantidade de curtidas das músicas com id=2 e com o id=3;
-- g) Atualizar o nome da música com o id=5;
-- h) Excluir a música com o id=4;
-- i) Exibir as músicas onde o gênero é diferente de funk;
-- j) Exibir os dados das músicas que tem curtidas maior ou igual a 20;
-- k) Descrever os campos da tabela mostrando a atualização do campo artista;
-- l) Limpar os dados da tabela;

CREATE TABLE Artista (
    idArtista int auto_increment primary key,
    artista varchar(40)
);

CREATE TABLE Genero (
    idGenero int auto_increment primary key,
    genero varchar(40)
);

CREATE TABLE Musica (
    idMusica int auto_increment primary key,
    titulo varchar(40),
    idArtista int,
    idGenero int,
    constraint foreign key fk_artista(idArtista) references Artista(idArtista) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    constraint foreign key fk_genero(idGenero) references Genero(idGenero) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 
-- Inserindo os Gêneros
-- 
INSERT INTO Genero (genero) VALUES ('Funk');
INSERT INTO Genero (genero) VALUES ('Pop');
INSERT INTO Genero (genero) VALUES ('Rock');
INSERT INTO Genero (genero) VALUES ('Hip-Hop');

-- 
-- Inserindo os Artistas
-- 
INSERT INTO Artista (artista) VALUES ('Anitta');
INSERT INTO Artista (artista) VALUES ('Ludmilla');
INSERT INTO Artista (artista) VALUES ('Maroon 5');
INSERT INTO Artista (artista) VALUES ('Drake');

-- 
-- Inserindo as Músicas
-- 
-- Artista: Anitta
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Envolver', (SELECT idArtista FROM Artista WHERE artista = 'Anitta'), (SELECT idGenero FROM Genero WHERE genero = 'Funk'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Bang Bang', (SELECT idArtista FROM Artista WHERE artista = 'Anitta'), (SELECT idGenero FROM Genero WHERE genero = 'Funk'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Medicina', (SELECT idArtista FROM Artista WHERE artista = 'Anitta'), (SELECT idGenero FROM Genero WHERE genero = 'Funk'));

-- Artista: Ludmilla
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Cheguei', (SELECT idArtista FROM Artista WHERE artista = 'Ludmilla'), (SELECT idGenero FROM Genero WHERE genero = 'Funk'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Braba', (SELECT idArtista FROM Artista WHERE artista = 'Ludmilla'), (SELECT idGenero FROM Genero WHERE genero = 'Funk'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('A Danada Sou Eu', (SELECT idArtista FROM Artista WHERE artista = 'Ludmilla'), (SELECT idGenero FROM Genero WHERE genero = 'Funk'));

-- Artista: Maroon 5
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Sugar', (SELECT idArtista FROM Artista WHERE artista = 'Maroon 5'), (SELECT idGenero FROM Genero WHERE genero = 'Pop'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Girls Like You', (SELECT idArtista FROM Artista WHERE artista = 'Maroon 5'), (SELECT idGenero FROM Genero WHERE genero = 'Pop'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Memories', (SELECT idArtista FROM Artista WHERE artista = 'Maroon 5'), (SELECT idGenero FROM Genero WHERE genero = 'Pop'));

-- Artista: Drake
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Started From The Bottom', (SELECT idArtista FROM Artista WHERE artista = 'Drake'), (SELECT idGenero FROM Genero WHERE genero = 'Hip-Hop'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('In My Feelings', (SELECT idArtista FROM Artista WHERE artista = 'Drake'), (SELECT idGenero FROM Genero WHERE genero = 'Hip-Hop'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Hotline Bling', (SELECT idArtista FROM Artista WHERE artista = 'Drake'), (SELECT idGenero FROM Genero WHERE genero = 'Hip-Hop'));

-- Artista: Queen
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Bohemian Rhapsody', (SELECT idArtista FROM Artista WHERE artista = 'Queen'), (SELECT idGenero FROM Genero WHERE genero = 'Rock'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('We Will Rock You', (SELECT idArtista FROM Artista WHERE artista = 'Queen'), (SELECT idGenero FROM Genero WHERE genero = 'Rock'));

-- Artista: The Rolling Stones
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Paint It Black', (SELECT idArtista FROM Artista WHERE artista = 'The Rolling Stones'), (SELECT idGenero FROM Genero WHERE genero = 'Rock'));
INSERT INTO Musica (titulo, idArtista, idGenero) VALUES ('Sympathy for the Devil', (SELECT idArtista FROM Artista WHERE artista = 'The Rolling Stones'), (SELECT idGenero FROM Genero WHERE genero = 'Rock'));


-- a) Exibir todos os dados da tabela.
SELECT
    *
FROM
    Musica m
JOIN
    Artista a ON a.idArtista = m.idArtista
JOIN 
    Genero g ON g.idGenero = g.idGenero;

-- b) Adicionar o campo curtidas do tipo int na tabela;
ALTER TABLE Musica ADD COLUMN curtidas int after titulo;

-- c) Atualizar o campo curtidas de todas as músicas inseridas;-- Atualizar o campo curtidas para cada música

-- Funk
UPDATE Musica SET curtidas = 500000 WHERE titulo = 'Envolver';
UPDATE Musica SET curtidas = 450000 WHERE titulo = 'Bang Bang';
UPDATE Musica SET curtidas = 400000 WHERE titulo = 'Medicina';
UPDATE Musica SET curtidas = 350000 WHERE titulo = 'Cheguei';
UPDATE Musica SET curtidas = 300000 WHERE titulo = 'Braba';
UPDATE Musica SET curtidas = 250000 WHERE titulo = 'A Danada Sou Eu';

-- Pop
UPDATE Musica SET curtidas = 600000 WHERE titulo = 'Sugar';
UPDATE Musica SET curtidas = 550000 WHERE titulo = 'Girls Like You';
UPDATE Musica SET curtidas = 530000 WHERE titulo = 'Memories';

-- Hip-Hop
UPDATE Musica SET curtidas = 700000 WHERE titulo = 'Started From The Bottom';
UPDATE Musica SET curtidas = 650000 WHERE titulo = 'In My Feelings';
UPDATE Musica SET curtidas = 620000 WHERE titulo = 'Hotline Bling';
UPDATE Musica SET curtidas = 590000 WHERE titulo = 'Started From The Bottom';

-- Rock
UPDATE Musica SET curtidas = 800000 WHERE titulo = 'Bohemian Rhapsody';
UPDATE Musica SET curtidas = 780000 WHERE titulo = 'We Will Rock You';
UPDATE Musica SET curtidas = 770000 WHERE titulo = 'Paint It Black';
UPDATE Musica SET curtidas = 750000 WHERE titulo = 'Sympathy for the Devil';

-- d) Modificar o campo artista do tamanho 40 para o tamanho 80;
ALTER TABLE Artista MODIFY artista varchar(80);

-- e) Atualizar a quantidade de curtidas da música com id=1;
UPDATE Musica SET curtidas = 800000 where idMusica = 1;

-- f) Atualizar a quantidade de curtidas das músicas com id=2 e com o id=3;
UPDATE Musica SET curtidas = 500000 where idMusica in (2,3);

-- g) Atualizar o nome da música com o id=5;
UPDATE Musica SET titulo = 'Nem On Nem Off' where idMusica = 5;

-- h) Excluir a música com o id=4;
DELETE FROM Musica where idMusica = 4;

-- i) Exibir as músicas onde o gênero é diferente de funk;
SELECT
    *
FROM
    Musica m
JOIN
    Artista a ON a.idArtista = m.idArtista
JOIN
    Genero g ON g.idGenero = m.idGenero
WHERE g.genero <> 'Funk';

-- j) Exibir os dados das músicas que tem curtidas maior ou igual a 400000;
SELECT
    *
FROM
    Musica m
JOIN
    Artista a ON a.idArtista = m.idArtista
JOIN
    Genero g ON g.idGenero = m.idGenero
WHERE m.curtidas >= 400000;

-- k) Descrever os campos da tabela mostrando a atualização do campo artista;
DESCRIBE Musica;
DESCRIBE Artista;
DESCRIBE Genero;

-- l) Limpar os dados da tabela;
SET foreign_key_checks = 0;
TRUNCATE Artista;
TRUNCATE Genero;
TRUNCATE Musica;
SET foreign_key_checks = 1;
SELECT * FROM Artista;
SELECT * FROM Genero;
SELECT * FROM Musica;


-- =========================================== END ATIVIDADE 02 ===================================================== --

-- ===========================================  ATIVIDADE 03 ===================================================== --
-- 3. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Criar a tabela chamada Filme para conter os dados: idFilme, título (tamanho 50), genero
-- (tamanho 40), diretor (tamanho 40), sendo que idFilme é a chave primária da tabela.
-- Inserir dados na tabela, procurando colocar um gênero de filme que tenha mais de um
-- filme, e um diretor, que tenha mais de um filme cadastrado. Procure inserir pelo menos
-- uns 7 filmes.
-- Execute os comandos para:
-- • Exibir todos os dados da tabela.
-- • Adicionar o campo protagonista do tipo varchar(50) na tabela;
-- • Atualizar o campo protagonista de todas os filmes inseridos;
-- • Modificar o campo diretor do tamanho 40 para o tamanho 150;
-- • Atualizar o diretor do filme com id=5;
-- • Atualizar o diretor dos filmes com id=2 e com o id=7;
-- • Atualizar o título do filme com o id=6;
-- • Excluir o filme com o id=3;
-- • Exibir os filmes em que o gênero é diferente de drama;
-- • Exibir os dados dos filmes que o gênero é igual ‘suspense’;
-- • Descrever os campos da tabela mostrando a atualização do campo protagonista e
-- diretor;
-- • Limpar os dados da tabela;

CREATE TABLE IF NOT EXISTS Diretor (
    idDiretor int auto_increment primary key,
    diretor varchar(40)
);

ALTER TABLE Genero MODIFY genero varchar(40);

CREATE TABLE IF NOT EXISTS Filme (
    idFilme int auto_increment primary key,
    titulo varchar(50),
    idDiretor int,
    idGenero int,
    constraint foreign key fk_diretor(idDiretor) references Diretor(idDiretor) 
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    constraint foreign key fk_genero(idGenero) references Genero(idGenero) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

--
-- Inserir Gêneros
--
INSERT INTO Genero (genero) VALUES ('Ação');
INSERT INTO Genero (genero) VALUES ('Comédia');
INSERT INTO Genero (genero) VALUES ('Drama');
INSERT INTO Genero (genero) VALUES ('Suspense');

--
-- Inserir Diretores
--
INSERT INTO Diretor (diretor) VALUES ('Steven Spielberg');
INSERT INTO Diretor (diretor) VALUES ('Martin Scorsese');
INSERT INTO Diretor (diretor) VALUES ('Quentin Tarantino');
INSERT INTO Diretor (diretor) VALUES ('Christopher Nolan');

--
-- Inserir Filmes para o Diretor Steven Spielberg
--
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Jurassic Park', 1, 1);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('E.T.', 1, 1);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('A Lista de Schindler', 1, 3);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Indiana Jones', 1, 1);

--
-- Inserir Filmes para o Diretor Martin Scorsese
--
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Taxi Driver', 2, 3);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Goodfellas', 2, 3);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('The Irishman', 2, 3);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('The Wolf of Wall Street', 2, 3);

--
-- Inserir Filmes para o Diretor Quentin Tarantino
--
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Pulp Fiction', 3, 2);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Kill Bill: Vol. 1', 3, 1);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Inglourious Basterds', 3, 1);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Django Unchained', 3, 1);

--
-- Inserir Filmes para o Diretor Christopher Nolan
--
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Inception', 4, 4);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('The Dark Knight', 4, 1);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Interstellar', 4, 4);
INSERT INTO Filme (titulo, idDiretor, idGenero) VALUES ('Dunkirk', 4, 4);


-- • Exibir todos os dados da tabela.
SELECT
    *
FROM
    Filme f
JOIN
    Diretor d ON d.idDiretor = f.idDiretor
JOIN
    Genero g ON g.idGenero = f.idGenero;

-- • Adicionar o campo protagonista do tipo varchar(50) na tabela;
ALTER TABLE Filme ADD COLUMN idArtista int after titulo;
ALTER TABLE Filme ADD FOREIGN KEY fk_artista(idArtista) REFERENCES Artista(idArtista) ON DELETE CASCADE ON UPDATE CASCADE;

-- • Atualizar o campo protagonista de todas os filmes inseridos;
INSERT INTO Artista (artista) VALUES 
('Harrison Ford'),
('Robert De Niro'),
('Leonardo DiCaprio'),
('Brad Pitt');


UPDATE Filme SET idArtista = 1 WHERE idFilme = 1;
UPDATE Filme SET idArtista = 1 WHERE idFilme = 2;
UPDATE Filme SET idArtista = 1 WHERE idFilme = 3;
UPDATE Filme SET idArtista = 1 WHERE idFilme = 4;
UPDATE Filme SET idArtista = 2 WHERE idFilme = 5;
UPDATE Filme SET idArtista = 2 WHERE idFilme = 6;
UPDATE Filme SET idArtista = 2 WHERE idFilme = 7;
UPDATE Filme SET idArtista = 2 WHERE idFilme = 8;
UPDATE Filme SET idArtista = 3 WHERE idFilme = 9;
UPDATE Filme SET idArtista = 3 WHERE idFilme = 10;
UPDATE Filme SET idArtista = 3 WHERE idFilme = 11;
UPDATE Filme SET idArtista = 3 WHERE idFilme = 12;
UPDATE Filme SET idArtista = 4 WHERE idFilme = 13;
UPDATE Filme SET idArtista = 4 WHERE idFilme = 14;
UPDATE Filme SET idArtista = 4 WHERE idFilme = 15;
UPDATE Filme SET idArtista = 4 WHERE idFilme = 16;

-- • Modificar o campo diretor do tamanho 40 para o tamanho 150;
ALTER TABLE Diretor MODIFY diretor varchar(150);

-- • Atualizar o diretor do filme com id=5;
UPDATE Filme SET idDiretor = 3 WHERE idFilme = 5;

-- • Atualizar o diretor dos filmes com id=2 e com o id=7;
UPDATE Filme SET idDiretor = 4 WHERE idFilme in (2,7);

-- • Atualizar o título do filme com o id=6;
UPDATE Filme SET titulo = 'The Irishman' WHERE idFilme = 6;

-- • Excluir o filme com o id=3;
DELETE FROM Filme WHERE idFilme = 3;

-- • Exibir os filmes em que o gênero é diferente de drama;
SELECT
    *
FROM
    Filme f
JOIN
    Diretor d ON d.idDiretor = f.idDiretor
JOIN
    Genero g ON g.idGenero = f.idGenero
WHERE g.genero <> 'Drama';

-- • Exibir os dados dos filmes que o gênero é igual ‘suspense’;
SELECT
    *
FROM
    Filme f
JOIN
    Diretor d ON d.idDiretor = f.idDiretor
JOIN
    Genero g ON g.idGenero = f.idGenero
WHERE g.genero <> 'Suspense';

-- • Descrever os campos da tabela mostrando a atualização do campo protagonista e diretor;
DESCRIBE Filme;
DESCRIBE Diretor;
DESCRIBE Genero;

-- • Limpar os dados da tabela;
SET foreign_key_checks = 0;
TRUNCATE Diretor;
TRUNCATE Genero;
TRUNCATE Filme;
SET foreign_key_checks = 1;

-- =========================================== END ATIVIDADE 03 ===================================================== --