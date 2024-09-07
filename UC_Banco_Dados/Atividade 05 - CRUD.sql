-- 5. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
-- Criar a tabela chamada Curso para conter os dados: idCurso, nome (tamanho 50), sigla
-- (tamanho 3), coordenador, sendo que idCurso é a chave primária da tabela.
-- Inserir dados na tabela, procure inserir pelo menos 3 cursos.
-- Execute os comandos para:
-- a) Exibir todos os dados da tabela.
-- b) Exibir apenas os coordenadores dos cursos.
-- c) Exibir apenas os dados dos cursos de uma determinada sigla.
-- d) Exibir os dados da tabela ordenados pelo nome do curso.
-- e) Exibir os dados da tabela ordenados pelo nome do coordenador em ordem
-- decrescente.
-- f) Exibir os dados da tabela, dos cursos cujo nome comece com uma determinada letra.
-- g) Exibir os dados da tabela, dos cursos cujo nome termine com uma determinada letra.
-- h) Exibir os dados da tabela, dos cursos cujo nome tenha como segunda letra uma
-- determinada letra.
-- i) Exibir os dados da tabela, dos cursos cujo nome tenha como penúltima letra uma
-- determinada letra.
-- j) Elimine a tabela.

USE sprint;

CREATE TABLE IF NOT EXISTS Coordenador (
    idCoordenador INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Curso (
    idCurso INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    sigla VARCHAR(3),
    idCoordenador INT,
    FOREIGN KEY (idCoordenador) REFERENCES coordenador(idCoordenador) ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO Coordenador (nome) VALUES ('João');
INSERT INTO Coordenador (nome) VALUES ('Maria');
INSERT INTO Coordenador (nome) VALUES ('José');

INSERT INTO Curso (nome, sigla, idCoordenador) VALUES ('Sistemas de Informação', 'SI', 1);
INSERT INTO Curso (nome, sigla, idCoordenador) VALUES ('Engenharia de Software', 'ES', 2);
INSERT INTO Curso (nome, sigla, idCoordenador) VALUES ('Análise e Desenvolvimento de Sistemas', 'ADS', 3);
INSERT INTO Curso (nome, sigla, idCoordenador) VALUES ('Ciência da Computação', 'CC', 1);


-- a) Exibir todos os dados da tabela.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador;

-- b) Exibir apenas os coordenadores dos cursos.
SELECT
    co.nome AS Coordenador
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador;

-- c) Exibir apenas os dados dos cursos de uma determinada sigla.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
WHERE
    c.sigla = 'SI';

-- d) Exibir os dados da tabela ordenados pelo nome do curso.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
ORDER BY
    c.nome;

-- e) Exibir os dados da tabela ordenados pelo nome do coordenador em ordem decrescente.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
ORDER BY
    c.nome DESC;

-- f) Exibir os dados da tabela, dos cursos cujo nome comece com uma determinada letra.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
WHERE
    c.nome LIKE 'A%';

-- g) Exibir os dados da tabela, dos cursos cujo nome termine com uma determinada letra.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
WHERE
    c.nome LIKE '%e';

-- h) Exibir os dados da tabela, dos cursos cujo nome tenha como segunda letra uma determinada letra.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
WHERE
    c.nome LIKE '_n%';

-- i) Exibir os dados da tabela, dos cursos cujo nome tenha como penúltima letra uma determinada letra.
SELECT
    *
FROM
    Curso c
JOIN
    Coordenador co ON c.idCoordenador = co.idCoordenador
WHERE
    c.nome LIKE '%r_';

-- j) Elimine a tabela.

DROP TABLE Curso;
DROP TABLE Coordenador;