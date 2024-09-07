-- 6. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Você vai criar uma tabela para armazenar os dados de revistas (como por ex: Veja, Isto é,
-- Epoca, Quatro Rodas, Claudia, etc).
-- Escreva e execute os comandos para:
-- • Criar a tabela chamada Revista para conter os campos: idRevista (int e chave
-- primária da tabela), nome (varchar, tamanho 40), categoria (varchar, tamanho 30). Os
-- valores de idRevista devem iniciar com o valor 1 e ser incrementado automaticamente
-- pelo sistema.
-- • Inserir 4 registros na tabela, mas sem informar a categoria.
-- Escreva e execute os comandos para:
-- • Exibir todos os dados da tabela.
-- • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
-- novamente para verificar se atualizou corretamente.
-- • Insira mais 3 registros completos.
-- • Exibir novamente os dados da tabela.
-- • Exibir a descrição da estrutura da tabela.
-- • Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres.
-- • Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o
-- tamanho da coluna categoria
-- • Acrescentar a coluna periodicidade à tabela, que é varchar(15).
-- • Exibir os dados da tabela.
-- • Excluir a coluna periodicidade da tabela.

USE sprint;

CREATE TABLE IF NOT EXISTS Categoria(
    idCategoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS Revista (
    idRevista INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40),
    idCategoria INT,
    FOREIGN KEY (idCategoria) REFERENCES Categoria(idCategoria) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Categoria (nome) VALUES ('Categoria 1');
INSERT INTO Categoria (nome) VALUES ('Categoria 2');
INSERT INTO Categoria (nome) VALUES ('Categoria 3');
INSERT INTO Categoria (nome) VALUES ('Categoria 4');

-- • Inserir 4 registros na tabela, mas sem informar a categoria.
INSERT INTO Revista (nome) VALUES ('Revista 1');
INSERT INTO Revista (nome) VALUES ('Revista 2');
INSERT INTO Revista (nome) VALUES ('Revista 3');
INSERT INTO Revista (nome) VALUES ('Revista 4');

-- • Exibir todos os dados da tabela.
SELECT
    *
FROM
    Revista r;

-- • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela novamente para verificar se atualizou corretamente.
UPDATE Revista SET idCategoria = 1 WHERE idRevista = 1;
UPDATE Revista SET idCategoria = 2 WHERE idRevista = 2;
UPDATE Revista SET idCategoria = 3 WHERE idRevista = 3;
UPDATE Revista SET idCategoria = 4 WHERE idRevista = 4;

SELECT
    *
FROM
    Revista r
JOIN
    Categoria c ON r.idCategoria = c.idCategoria;

-- • Insira mais 3 registros completos.
INSERT INTO Revista (nome, idCategoria) VALUES ('Revista 5', 1);
INSERT INTO Revista (nome, idCategoria) VALUES ('Revista 6', 2);
INSERT INTO Revista (nome, idCategoria) VALUES ('Revista 7', 3);

-- • Exibir novamente os dados da tabela.
SELECT
    *
FROM
    Revista r
JOIN
    Categoria c ON r.idCategoria = c.idCategoria;

-- • Exibir a descrição da estrutura da tabela.
DESCRIBE Revista;
DESCRIBE Categoria;

-- • Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres.
ALTER TABLE Categoria MODIFY COLUMN nome VARCHAR(40);

-- • Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o tamanho da coluna categoria
DESCRIBE Revista;
DESCRIBE Categoria;

-- • Acrescentar a coluna periodicidade à tabela, que é varchar(15).
ALTER TABLE Revista ADD COLUMN periodicidade VARCHAR(15) AFTER nome;

-- • Exibir os dados da tabela.
SELECT
    *
FROM
    Revista r
JOIN
    Categoria c ON r.idCategoria = c.idCategoria;

-- • Excluir a coluna periodicidade da tabela.
ALTER TABLE Revista DROP COLUMN periodicidade;